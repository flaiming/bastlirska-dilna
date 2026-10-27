// Kolecko k auticku na gumu (odlehcene: rafek + dno + naboj), na 3mm spejli
// Export z prikazove radky, napr.:
//   openscad -D 'diameter=45' -D 'style="louky"' -o kolo.stl kolecko.scad

diameter = 30;      // prumer kola: 30 / 45 / 60
height   = 8;       // sirka kola (tloustka): 8 / 10

// vzhled dna:
//   "zadne"   = plne dno
//   "kruhy"   = kulate odlehcovaci otvory (jen kdyz se vejdou)
//   "louky"   = rovne louky jako u jednoducheho kola
//   "zahnute" = zahnute louky
//   "okna"    = louky rozsirujici se k rafku, okna jako u disku auta
style = "louky";

rod = 3.46;         // otvor pro osu (3mm spejle): 3.4 tesne, 3.5 akorat ale prokluzuje, 3.6 uplne volne

wall      = 2;      // tloustka rafku
floor_h   = 2;      // tloustka dna (stredove steny)
hub_wall  = 2.5;    // tloustka steny naboje kolem osy
hub_collar = 1.5;   // plny prstenec dna kolem naboje (louky nedrzi jen na tenkem naboji)

// drazka po obvodu na gumicku = pneumatika (PLA klouze)
groove       = true;
groove_w     = 3;   // sirka drazky nahore, dno = groove_w - groove_depth
groove_depth = 0.5; // s rovnou spodni stenou staci (driv 0.5 s oboustrannym zkosenim gumicky sjizdely)

hole_count  = 5;    // pocet otvoru pro styl "kruhy"
spoke_count = 6;    // pocet louk pro styly "louky" a "zahnute"
spoke_w     = max(2.5, diameter / 15);  // sirka louky (30mm: 2.5, 45mm: 3, 60mm: 4)
spoke_twist = 50;   // o kolik stupnu se zahnuta louka stoci od naboje k rafku
window_count = 5;   // pocet oken pro styl "okna"
fillet      = 1;    // zaobleni rohu otvoru

chamfer = 0.5;      // srazeni hran (proti elephant foot + snazsi nasunuti na osu)
$fn = 100;

r     = diameter / 2;
rim   = wall + (groove ? groove_depth : 0);   // rafek je silnejsi o hloubku drazky
inner = r - rim;                              // vnitrni polomer rafku
hub_r = rod / 2 + hub_wall;

module chamfered_disc(d, h, c) {
    hull() {
        translate([0, 0, c]) cylinder(d=d, h=h - 2*c);
        cylinder(d=d - 2*c, h=h);
    }
}

module tire_groove() {
    // spodni stena rovna (tiskne se bez problemu), horni zkosena 45 st. -> bez podpor
    // ostra spodni hrana gumicku lip drzi
    if (groove) {
        z0 = (height - groove_w) / 2;
        rotate_extrude()
        polygon([
            [r + 1,            z0 - 1],
            [r,                z0 - 1],
            [r,                z0],
            [r - groove_depth, z0],
            [r - groove_depth, z0 + groove_w - groove_depth],
            [r,                z0 + groove_w],
            [r,                z0 + groove_w + 1],
            [r + 1,            z0 + groove_w + 1],
        ]);
    }
}

module axle_hole() {
    translate([0, 0, -1]) cylinder(d=rod, h=height + 2);
    // zkoseni vstupu z obou stran
    translate([0, 0, -0.01]) cylinder(d1=rod + 2*chamfer, d2=rod, h=chamfer);
    translate([0, 0, height - chamfer + 0.01]) cylinder(d1=rod, d2=rod + 2*chamfer, h=chamfer);
}

// mezikruzi mezi nabojem a rafkem, ze ktereho se vyrezavaji otvory
module floor_ring() {
    difference() {
        circle(r=inner);
        circle(r=hub_r + hub_collar);
    }
}

module straight_spokes() {
    for (i = [0 : spoke_count - 1])
        rotate(i * 360 / spoke_count)
        translate([0, -spoke_w / 2]) square([r, spoke_w]);
}

module curved_spokes() {
    steps = 12;
    for (i = [0 : spoke_count - 1])
        rotate(i * 360 / spoke_count)
        for (s = [0 : steps - 1]) hull() {
            for (t = [s, s + 1] / steps) {
                rr = hub_r - 1 + t * (inner - hub_r + 2);
                rotate(t * spoke_twist) translate([rr, 0]) circle(d=spoke_w, $fn=24);
            }
        }
}

module tapered_spokes() {
    for (i = [0 : window_count - 1])
        rotate(i * 360 / window_count)
        hull() {
            translate([hub_r, 0]) circle(d=spoke_w, $fn=24);
            translate([inner, 0]) circle(d=spoke_w * 2.5, $fn=24);
        }
}

module round_holes() {
    gap = inner - hub_r;                   // prostor mezi nabojem a rafkem
    rc  = hub_r + gap / 2;                 // polomer, na kterem lezi stredy otvoru
    // otvor nesmi byt vetsi nez mezera ani nesmi sezrat paprsky mezi otvory
    hole_d = min(gap - 2*wall, 2 * PI * rc / hole_count - 2*wall*2);
    if (hole_d >= 4)
        for (i = [0 : hole_count - 1])
            rotate(i * 360 / hole_count)
            translate([rc, 0]) circle(d=hole_d, $fn=40);
}

// 2D tvar otvoru ve dne podle zvoleneho stylu
module floor_cutouts_2d() {
    if (style == "kruhy") {
        round_holes();
    } else if (style == "louky" || style == "zahnute" || style == "okna") {
        // zaobleni rohu oken = hladke prechody louk do rafku a naboje
        offset(r=fillet) offset(r=-fillet)
        difference() {
            floor_ring();
            if (style == "louky")   straight_spokes();
            if (style == "zahnute") curved_spokes();
            if (style == "okna")    tapered_spokes();
        }
    }
}

module wheel() {
    difference() {
        chamfered_disc(diameter, height, chamfer);

        difference() {
            translate([0, 0, floor_h]) cylinder(r=inner, h=height);
            cylinder(r=hub_r, h=height + 1);
        }
        translate([0, 0, -1]) linear_extrude(floor_h + 2) floor_cutouts_2d();

        tire_groove();
        axle_hole();
    }
}

wheel();
