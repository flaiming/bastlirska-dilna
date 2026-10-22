// Excentr pro vibrobota (karta 05): nalisuje se na hřídel 2 mm motoru z Dratek.cz,
// do ramene se zašroubuje šroubek M3 (samořezně do plastu), případně s maticemi jako závažím.
// Tisk naležato (hřídel svisle), bez podpěr. Export: openscad -D 'dil="excentr"' -o excentr.stl excentr.scad

dil = "excentr";        // "excentr" nebo "zkouska" (destička s otvory na vyzkoušení lisování)

hridel_d   = 1.9;       // otvor pro hřídel 2 mm; přesnou hodnotu vybrat podle zkušební destičky
naboj_d    = 6;         // vnější průměr náboje
naboj_h    = 6;         // délka náboje (kolik se nasune na hřídel)
rameno_t   = 3;         // tloušťka ramene
rameno_w   = 7;         // šířka ramene
sroub_r    = 6;         // vzdálenost šroubku od osy = jak moc „excentrický“
sroub_d    = 2.6;       // otvor pro samořezný M3 do PLA/PETG

zkouska_d  = [1.7, 1.8, 1.9, 2.0, 2.1];

$fn = 64;

module excentr() {
    difference() {
        union() {
            cylinder(d = naboj_d, h = naboj_h);
            hull() {
                cylinder(d = rameno_w, h = rameno_t);
                translate([sroub_r, 0, 0]) cylinder(d = rameno_w, h = rameno_t);
            }
        }
        translate([0, 0, -1]) cylinder(d = hridel_d, h = naboj_h + 2);
        translate([sroub_r, 0, -1]) cylinder(d = sroub_d, h = rameno_t + 2);
    }
}

module zkouska() {
    krok = 9;
    difference() {
        union() {
            translate([-krok / 2, -6, 0]) cube([krok * len(zkouska_d), 12, 2]);
            for (i = [0 : len(zkouska_d) - 1])
                translate([i * krok, 2, 0]) cylinder(d = naboj_d, h = naboj_h);
        }
        for (i = [0 : len(zkouska_d) - 1]) {
            translate([i * krok, 2, -1]) cylinder(d = zkouska_d[i], h = naboj_h + 2);
            translate([i * krok, -4, 1.4])
                linear_extrude(1) text(str(zkouska_d[i]), size = 2.2, halign = "center", valign = "center");
        }
    }
}

if (dil == "zkouska") zkouska(); else excentr();
