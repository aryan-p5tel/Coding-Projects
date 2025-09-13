#for all elements in the periodic table, return the atomic weight and group

def element_info(info):
   
#includes an example of each format


    # Alkali metals
    if info == "Li" or info == "Lithium" or info == "Alkali metals":
        return "Element: Lithium\nAtomic weight: 6.94\nGroup: Alkali metals"
    elif info == "Na" or info == "Sodium" or info == "Alkali metals":
        return "Element: Sodium\nAtomic weight: 22.99\nGroup: Alkali metals"
    elif info == "K" or info == "Potassium" or info == "Alkali metals":
        return "Element: Potassium\nAtomic weight: 39.10\nGroup: Alkali metals"
    elif info == "Rb" or info == "Rubidium" or info == "Alkali metals":
        return "Element: Rubidium\nAtomic weight: 85.47\nGroup: Alkali metals"
    elif info == "Cs" or info == "Caesium" or info == "Alkali metals":
        return "Element: Caesium\nAtomic weight: 132.91\nGroup: Alkali metals"
    elif info == "Fr" or info == "Francium" or info == "Alkali metals":
        return "Element: Francium\nAtomic weight: 223\nGroup: Alkali metals"

    # Alkaline earth metals
    elif info == "Be" or info == "Beryllium" or info == "Alkaline earth metals":
        return "Element: Beryllium\nAtomic weight: 9.01\nGroup: Alkaline earth metals"
    elif info == "Mg" or info == "Magnesium" or info == "Alkaline earth metals":
        return "Element: Magnesium\nAtomic weight: 24.31\nGroup: Alkaline earth metals"
    elif info == "Ca" or info == "Calcium" or info == "Alkaline earth metals":
        return "Element: Calcium\nAtomic weight: 40.08\nGroup: Alkaline earth metals"
    elif info == "Sr" or info == "Strontium" or info == "Alkaline earth metals":
        return "Element: Strontium\nAtomic weight: 87.62\nGroup: Alkaline earth metals"
    elif info == "Ba" or info == "Barium" or info == "Alkaline earth metals":
        return "Element: Barium\nAtomic weight: 137.33\nGroup: Alkaline earth metals"
    elif info == "Ra" or info == "Radium" or info == "Alkaline earth metals":
        return "Element: Radium\nAtomic weight: 226\nGroup: Alkaline earth metals"

    # Transition metals
    elif info == "Sc" or info == "Scandium" or info == "Transition metals":
        return "Element: Scandium\nAtomic weight: 44.96\nGroup: Transition metals"
    elif info == "Ti" or info == "Titanium" or info == "Transition metals":
        return "Element: Titanium\nAtomic weight: 47.87\nGroup: Transition metals"
    elif info == "V" or info == "Vanadium" or info == "Transition metals":
        return "Element: Vanadium\nAtomic weight: 50.94\nGroup: Transition metals"
    elif info == "Cr" or info == "Chromium" or info == "Transition metals":
        return "Element: Chromium\nAtomic weight: 52.00\nGroup: Transition metals"
    elif info == "Mn" or info == "Manganese" or info == "Transition metals":
        return "Element: Manganese\nAtomic weight: 54.94\nGroup: Transition metals"
    elif info == "Fe" or info == "Iron" or info == "Transition metals":
        return "Element: Iron\nAtomic weight: 55.85\nGroup: Transition metals"
    elif info == "Co" or info == "Cobalt" or info == "Transition metals":
        return "Element: Cobalt\nAtomic weight: 58.93\nGroup: Transition metals"
    elif info == "Ni" or info == "Nickel" or info == "Transition metals":
        return "Element: Nickel\nAtomic weight: 58.69\nGroup: Transition metals"
    elif info == "Cu" or info == "Copper" or info == "Transition metals":
        return "Element: Copper\nAtomic weight: 63.55\nGroup: Transition metals"
    elif info == "Zn" or info == "Zinc" or info == "Transition metals":
        return "Element: Zinc\nAtomic weight: 65.38\nGroup: Transition metals"
    elif info == "Y" or info == "Yttrium" or info == "Transition metals":
        return "Element: Yttrium\nAtomic weight: 88.91\nGroup: Transition metals"
    elif info == "Zr" or info == "Zirconium" or info == "Transition metals":
        return "Element: Zirconium\nAtomic weight: 91.22\nGroup: Transition metals"
    elif info == "Nb" or info == "Niobium" or info == "Transition metals":
        return "Element: Niobium\nAtomic weight: 92.91\nGroup: Transition metals"
    elif info == "Mo" or info == "Molybdenum" or info == "Transition metals":
        return "Element: Molybdenum\nAtomic weight: 95.95\nGroup: Transition metals"
    elif info == "Tc" or info == "Technetium" or info == "Transition metals":
        return "Element: Technetium\nAtomic weight: 98\nGroup: Transition metals"
    elif info == "Ru" or info == "Ruthenium" or info == "Transition metals":
        return "Element: Ruthenium\nAtomic weight: 101.07\nGroup: Transition metals"
    elif info == "Rh" or info == "Rhodium" or info == "Transition metals":
        return "Element: Rhodium\nAtomic weight: 102.91\nGroup: Transition metals"
    elif info == "Pd" or info == "Palladium" or info == "Transition metals":
        return "Element: Palladium\nAtomic weight: 106.42\nGroup: Transition metals"
    elif info == "Ag" or info == "Silver" or info == "Transition metals":
        return "Element: Silver\nAtomic weight: 107.87\nGroup: Transition metals"
    elif info == "Cd" or info == "Cadmium" or info == "Transition metals":
        return "Element: Cadmium\nAtomic weight: 112.41\nGroup: Transition metals"
    elif info == "Hf" or info == "Hafnium" or info == "Transition metals":
        return "Element: Hafnium\nAtomic weight: 178.49\nGroup: Transition metals"
    elif info == "Ta" or info == "Tantalum" or info == "Transition metals":
        return "Element: Tantalum\nAtomic weight: 180.95\nGroup: Transition metals"
    elif info == "W" or info == "Tungsten" or info == "Transition metals":
        return "Element: Tungsten\nAtomic weight: 183.84\nGroup: Transition metals"
    elif info == "Re" or info == "Rhenium" or info == "Transition metals":
        return "Element: Rhenium\nAtomic weight: 186.21\nGroup: Transition metals"
    elif info == "Os" or info == "Osmium" or info == "Transition metals":
        return "Element: Osmium\nAtomic weight: 190.23\nGroup: Transition metals"
    elif info == "Ir" or info == "Iridium" or info == "Transition metals":
        return "Element: Iridium\nAtomic weight: 192.22\nGroup: Transition metals"
    elif info == "Pt" or info == "Platinum" or info == "Transition metals":
        return "Element: Platinum\nAtomic weight: 195.08\nGroup: Transition metals"
    elif info == "Au" or info == "Gold" or info == "Transition metals":
        return "Element: Gold\nAtomic weight: 196.97\nGroup: Transition metals"
    elif info == "Hg" or info == "Mercury" or info == "Transition metals":
        return "Element: Mercury\nAtomic weight: 200.59\nGroup: Transition metals"
    elif info == "Rf" or info == "Rutherfordium" or info == "Transition metals":
        return "Element: Rutherfordium\nAtomic weight: 267\nGroup: Transition metals"
    elif info == "Db" or info == "Dubnium" or info == "Transition metals":
        return "Element: Dubnium\nAtomic weight: 270\nGroup: Transition metals"
    elif info == "Sg" or info == "Seaborgium" or info == "Transition metals":
        return "Element: Seaborgium\nAtomic weight: 271\nGroup: Transition metals"
    elif info == "Bh" or info == "Bohrium" or info == "Transition metals":
        return "Element: Bohrium\nAtomic weight: 270\nGroup: Transition metals"
    elif info == "Hs" or info == "Hassium" or info == "Transition metals":
        return "Element: Hassium\nAtomic weight: 277\nGroup: Transition metals"

    # Post-transition metals
    elif info == "Al" or info == "Aluminium" or info == "Post-transition metals":
        return "Element: Aluminium\nAtomic weight: 26.98\nGroup: Post-transition metals"
    elif info == "Ga" or info == "Gallium" or info == "Post-transition metals":
        return "Element: Gallium\nAtomic weight: 69.72\nGroup: Post-transition metals"
    elif info == "In" or info == "Indium" or info == "Post-transition metals":
        return "Element: Indium\nAtomic weight: 114.82\nGroup: Post-transition metals"
    elif info == "Sn" or info == "Tin" or info == "Post-transition metals":
        return "Element: Tin\nAtomic weight: 118.71\nGroup: Post-transition metals"
    elif info == "Tl" or info == "Thallium" or info == "Post-transition metals":
        return "Element: Thallium\nAtomic weight: 204.38\nGroup: Post-transition metals"
    elif info == "Pb" or info == "Lead" or info == "Post-transition metals":
        return "Element: Lead\nAtomic weight: 207.2\nGroup: Post-transition metals"
    elif info == "Bi" or info == "Bismuth" or info == "Post-transition metals":
        return "Element: Bismuth\nAtomic weight: 208.98\nGroup: Post-transition metals"
    elif info == "Nh" or info == "Nihonium" or info == "Post-transition metals":
        return "Element: Nihonium\nAtomic weight: 286\nGroup: Post-transition metals"
    elif info == "Fl" or info == "Flerovium" or info == "Post-transition metals":
        return "Element: Flerovium\nAtomic weight: 289\nGroup: Post-transition metals"
    elif info == "Mc" or info == "Moscovium" or info == "Post-transition metals":
        return "Element: Moscovium\nAtomic weight: 290\nGroup: Post-transition metals"
    elif info == "Lv" or info == "Livermorium" or info == "Post-transition metals":
        return "Element: Livermorium\nAtomic weight: 293\nGroup: Post-transition metals"

    # Metalloids
    elif info == "B" or info == "Boron" or info == "Metalloids":
        return "Element: Boron\nAtomic weight: 10.81\nGroup: Metalloids"
    elif info == "Si" or info == "Silicon" or info == "Metalloids":
        return "Element: Silicon\nAtomic weight: 28.09\nGroup: Metalloids"
    elif info == "Ge" or info == "Germanium" or info == "Metalloids":
        return "Element: Germanium\nAtomic weight: 72.63\nGroup: Metalloids"
    elif info == "As" or info == "Arsenic" or info == "Metalloids":
        return "Element: Arsenic\nAtomic weight: 74.92\nGroup: Metalloids"
    elif info == "Sb" or info == "Antimony" or info == "Metalloids":
        return "Element: Antimony\nAtomic weight: 121.76\nGroup: Metalloids"
    elif info == "Te" or info == "Tellurium" or info == "Metalloids":
        return "Element: Tellurium\nAtomic weight: 127.60\nGroup: Metalloids"
    elif info == "Po" or info == "Polonium" or info == "Metalloids":
        return "Element: Polonium\nAtomic weight: 209\nGroup: Metalloids"

    # Nonmetals
    elif info == "H" or info == "Hydrogen" or info == "Nonmetals":
        return "Element: Hydrogen\nAtomic weight: 1.01\nGroup: Nonmetals"
    elif info == "C" or info == "Carbon" or info == "Nonmetals":
        return "Element: Carbon\nAtomic weight: 12.01\nGroup: Nonmetals"
    elif info == "N" or info == "Nitrogen" or info == "Nonmetals":
        return "Element: Nitrogen\nAtomic weight: 14.01\nGroup: Nonmetals"
    elif info == "O" or info == "Oxygen" or info == "Nonmetals":
        return "Element: Oxygen\nAtomic weight: 16.00\nGroup: Nonmetals"
    elif info == "P" or info == "Phosphorus" or info == "Nonmetals":
        return "Element: Phosphorus\nAtomic weight: 30.97\nGroup: Nonmetals"
    elif info == "S" or info == "Sulfur" or info == "Nonmetals":
        return "Element: Sulfur\nAtomic weight: 32.07\nGroup: Nonmetals"
    elif info == "Se" or info == "Selenium" or info == "Nonmetals":
        return "Element: Selenium\nAtomic weight: 78.96\nGroup: Nonmetals"

    # Halogens
    elif info == "F" or info == "Fluorine" or info == "Halogens":
        return "Element: Fluorine\nAtomic weight: 18.99\nGroup: Halogens"
    elif info == "Cl" or info == "Chlorine" or info == "Halogens":
        return "Element: Chlorine\nAtomic weight: 35.45\nGroup: Halogens"
    elif info == "Br" or info == "Bromine" or info == "Halogens":
        return "Element: Bromine\nAtomic weight: 79.90\nGroup: Halogens"
    elif info == "I" or info == "Iodine" or info == "Halogens":
        return "Element: Iodine\nAtomic weight: 126.90\nGroup: Halogens"
    elif info == "At" or info == "Astatine" or info == "Halogens":
        return "Element: Astatine\nAtomic weight: 210\nGroup: Halogens"
    elif info == "Ts" or info == "Tennessine" or info == "Halogens":
        return "Element: Tennessine\nAtomic weight: 294\nGroup: Halogens"

    # Noble gases
    elif info == "He" or info == "Helium" or info == "Noble gases":
        return "Element: Helium\nAtomic weight: 4.00\nGroup: Noble gases"
    elif info == "Ne" or info == "Neon" or info == "Noble gases":
        return "Element: Neon\nAtomic weight: 20.18\nGroup: Noble gases"
    elif info == "Ar" or info == "Argon" or info == "Noble gases":
        return "Element: Argon\nAtomic weight: 39.95\nGroup: Noble gases"
    elif info == "Kr" or info == "Krypton" or info == "Noble gases":
        return "Element: Krypton\nAtomic weight: 83.80\nGroup: Noble gases"
    elif info == "Xe" or info == "Xenon" or info == "Noble gases":
        return "Element: Xenon\nAtomic weight: 131.29\nGroup: Noble gases"
    elif info == "Rn" or info == "Radon" or info == "Noble gases":
        return "Element: Radon\nAtomic weight: 222\nGroup: Noble gases"
    elif info == "Og" or info == "Oganesson" or info == "Noble gases":
        return "Element: Oganesson\nAtomic weight: 294\nGroup: Noble gases"

    # Lanthanides
    elif info == "La" or info == "Lanthanum" or info == "Lanthanides":
        return "Element: Lanthanum\nAtomic weight: 138.91\nGroup: Lanthanides"
    elif info == "Ce" or info == "Cerium" or info == "Lanthanides":
        return "Element: Cerium\nAtomic weight: 140.12\nGroup: Lanthanides"
    elif info == "Pr" or info == "Praseodymium" or info == "Lanthanides":
        return "Element: Praseodymium\nAtomic weight: 140.91\nGroup: Lanthanides"
    elif info == "Nd" or info == "Neodymium" or info == "Lanthanides":
        return "Element: Neodymium\nAtomic weight: 144.24\nGroup: Lanthanides"
    elif info == "Pm" or info == "Promethium" or info == "Lanthanides":
        return "Element: Promethium\nAtomic weight: 145\nGroup: Lanthanides"
    elif info == "Sm" or info == "Samarium" or info == "Lanthanides":
        return "Element: Samarium\nAtomic weight: 150.36\nGroup: Lanthanides"
    elif info == "Eu" or info == "Europium" or info == "Lanthanides":
        return "Element: Europium\nAtomic weight: 151.96\nGroup: Lanthanides"
    elif info == "Gd" or info == "Gadolinium" or info == "Lanthanides":
        return "Element: Gadolinium\nAtomic weight: 157.25\nGroup: Lanthanides"
    elif info == "Tb" or info == "Terbium" or info == "Lanthanides":
        return "Element: Terbium\nAtomic weight: 158.93\nGroup: Lanthanides"
    elif info == "Dy" or info == "Dysprosium" or info == "Lanthanides":
        return "Element: Dysprosium\nAtomic weight: 162.50\nGroup: Lanthanides"
    elif info == "Ho" or info == "Holmium" or info == "Lanthanides":
        return "Element: Holmium\nAtomic weight: 164.93\nGroup: Lanthanides"
    elif info == "Er" or info == "Erbium" or info == "Lanthanides":
        return "Element: Erbium\nAtomic weight: 167.26\nGroup: Lanthanides"
    elif info == "Tm" or info == "Thulium" or info == "Lanthanides":
        return "Element: Thulium\nAtomic weight: 168.93\nGroup: Lanthanides"
    elif info == "Yb" or info == "Ytterbium" or info == "Lanthanides":
        return "Element: Ytterbium\nAtomic weight: 173.05\nGroup: Lanthanides"
    elif info == "Lu" or info == "Lutetium" or info == "Lanthanides":
        return "Element: Lutetium\nAtomic weight: 174.97\nGroup: Lanthanides"

    # Actinides
    elif info == "Ac" or info == "Actinium" or info == "Actinides":
        return "Element: Actinium\nAtomic weight: 227\nGroup: Actinides"
    elif info == "Th" or info == "Thorium" or info == "Actinides":
        return "Element: Thorium\nAtomic weight: 232.04\nGroup: Actinides"
    elif info == "Pa" or info == "Protactinium" or info == "Actinides":
        return "Element: Protactinium\nAtomic weight: 231.04\nGroup: Actinides"
    elif info == "U" or info == "Uranium" or info == "Actinides":
        return "Element: Uranium\nAtomic weight: 238.03\nGroup: Actinides"
    elif info == "Np" or info == "Neptunium" or info == "Actinides":
        return "Element: Neptunium\nAtomic weight: 237\nGroup: Actinides"
    elif info == "Pu" or info == "Plutonium" or info == "Actinides":
        return "Element: Plutonium\nAtomic weight: 244\nGroup: Actinides"
    elif info == "Am" or info == "Americium" or info == "Actinides":
        return "Element: Americium\nAtomic weight: 243\nGroup: Actinides"
    elif info == "Cm" or info == "Curium" or info == "Actinides":
        return "Element: Curium\nAtomic weight: 247\nGroup: Actinides"
    elif info == "Bk" or info == "Berkelium" or info == "Actinides":
        return "Element: Berkelium\nAtomic weight: 247\nGroup: Actinides"
    elif info == "Cf" or info == "Californium" or info == "Actinides":
        return "Element: Californium\nAtomic weight: 251\nGroup: Actinides"
    elif info == "Es" or info == "Einsteinium" or info == "Actinides":
        return "Element: Einsteinium\nAtomic weight: 252\nGroup: Actinides"
    elif info == "Fm" or info == "Fermium" or info == "Actinides":
        return "Element: Fermium\nAtomic weight: 257\nGroup: Actinides"
    elif info == "Md" or info == "Mendelevium" or info == "Actinides":
        return "Element: Mendelevium\nAtomic weight: 258\nGroup: Actinides"
    elif info == "No" or info == "Nobelium" or info == "Actinides":
        return "Element: Nobelium\nAtomic weight: 259\nGroup: Actinides"
    elif info == "Lr" or info == "Lawrencium" or info == "Actinides":
        return "Element: Lawrencium\nAtomic weight: 262\nGroup: Actinides"

    else:
        return "Element not found"

info = "Na"  # Example: change "Na" to any element symbol or name you want to look up
details = element_info(info)
print(details)

