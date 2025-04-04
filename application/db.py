import sqlite3

# Connexion à la base de données
con = sqlite3.connect("world_of_warships.db")
cur = con.cursor()

# Création des tables
cur.execute("""
Create table if not exists Tier (
            id integer Primary key autoincrement,
            valeur real
)
""")

cur.execute("""
Create table if not exists Class (
            id integer primary key autoincrement,
            name text
)
""")

cur.execute("""
Create table if not exists Nation (
            id integer primary key autoincrement,
            name text                     
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Navires (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Ship TEXT,
    Tier_id INTEGER,
    Class_id integer,
    Nation_id integer,
    Length REAL,
    Beam REAL,
    Tonnage REAL,
    Health INTEGER,
    Detect_by_sea REAL,
    Detect_by_air REAL,
    Max_speed REAL,
    Acceleration REAL,
    Rudder_shift REAL,
    Turning_circle REAL,
    Repair_percentage REAL,
    Gun_range_percentage REAL,
    Torpedo_protection_percentage REAL,
    Fire_resistance_percentage REAL,
    foreign key (Tier_id) References Tier(id),
    foreign key (Class_id) references Class(id),
    foreign key (Nation_id) references Nation(id)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Navires_premium (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Ship TEXT,
    Tier_id INTEGER,
    Class_id integer,
    Nation_id integer,
    Length REAL,
    Beam REAL,
    Tonnage REAL,
    Health INTEGER,
    Detect_by_sea REAL,
    Detect_by_air REAL,
    Max_speed REAL,
    Acceleration REAL,
    Rudder_shift REAL,
    Turning_circle REAL,
    Repair_percentage REAL,
    Gun_range_percentage REAL,
    Torpedo_protection_percentage REAL,
    Fire_resistance_percentage REAL,
    foreign key (Tier_id) References Tier(id),
    foreign key (Class_id) references Class(id),
    foreign key (Nation_id) references Nation(id)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Navires_test (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Ship TEXT,
    Tier_id INTEGER,
    Class_id integer,
    Nation_id integer,
    Length REAL,
    Beam REAL,
    Tonnage REAL,
    Health INTEGER,
    Detect_by_sea REAL,
    Detect_by_air REAL,
    Max_speed REAL,
    Acceleration REAL,
    Rudder_shift REAL,
    Turning_circle REAL,
    Repair_percentage REAL,
    Gun_range_percentage REAL,
    Torpedo_protection_percentage REAL,
    Fire_resistance_percentage REAL,
    foreign key (Tier_id) References Tier(id),
    foreign key (Class_id) references Class(id),
    foreign key (Nation_id) references Nation(id)
)
""")

cur.execute("""
Create table if not exists Capa_de_polonger ( 
            id integer primary key autoincrement,
            Ship text,
            Tier_id integer,
            Class_id integer,
            Nation_id integer,
            Detectability real,
            Submerged_speed real,
            Diving_plane_shift real,
            Diving_speed real,
            Dive_capacity real,
            Depletion_rate real,
            Recharge_rate real,
            foreign key (Tier_id) References Tier(id),
            foreign key (Class_id) references Class(id),
            foreign key (Nation_id) references Nation(id)        
)
""")

cur.execute("""
Create table if not exists Main_Battery (
            id integer primary key autoincrement,
            Ship text,
            Tier_id integer,
            Class_id integer,
            Nation_id integer,
            Description text,
            AP_DPM real,
            HE_DPM real,
            SAP_DPM real,
            AP_Salvo real,
            HE_Salvo real,
            SAP_Salvo real,
            Range real,
            Reload real,
            Turn_180 real,
            Horizontal_dispetion real,
            Vertical_dispertion real,
            Sigma real,
            Flight_time real,
            Shells_per_minute real,
            foreign key (Tier_id) References Tier(id),
            foreign key (Class_id) references Class(id),
            foreign key (Nation_id) references Nation(id) 
)
""")

cur.execute("""
Create table if not exists AP_Shells (
            id integer primary key autoincrement,
            Ship text,
            Tier_id integer,
            Class_id integer,
            Nation_id integer,
            Description text,
            Weight real,
            Damage real,
            Initial_speed real,
            Drag_coeff real,
            Flight_time real,
            Impact_speed real,
            Impact_angle real,
            Krupp real,
            Penetration real,
            Overwatch real,
            Ricochet text,
            Thershold real,
            Fuse_time real,
            foreign key (Tier_id) References Tier(id),
            foreign key (Class_id) references Class(id),
            foreign key (Nation_id) references Nation(id) 
)
""")

cur.execute ("""
Create table if not exists HE_Shells (
             id integer primary key autoincrement,
             Ship text,
             Tier_id integer,
             Class_id integer,
             Nation_id integer,
             Description text,
             Weight real,
             Damage real,
             Initial_speed real,
             Drag_coeff real,
             Flight_time real,
             impact_speed real,
             Impact_angle real,
             Penetration real,
             Fire_chance real,
             Fires_per_minute real,
            foreign key (Tier_id) References Tier(id),
            foreign key (Class_id) references Class(id),
            foreign key (Nation_id) references Nation(id) 
)
""")

cur.execute ("""
Create table if not exists SAP_Shells (
             id integer primary key autoincrement,
             Ship text,
             Tier_id integer,
             Class_id integer,
             Nation_id integer,
             Description text,
             Weight real,
             Damage real,
             Initial_speed real,
             Drag_coeff real,
             Flight_time real,
             Impact_speed real,
             Impact_angle real,
             Pernetration real,
             Ricochet text,
            foreign key (Tier_id) References Tier(id),
            foreign key (Class_id) references Class(id),
            foreign key (Nation_id) references Nation(id) 
)
""")

cur.execute("""
Create table if not exists Secondaries (
            id integer primary key autoincrement,
            Ship text,
            Tier_id integer,
            Class_id integer,
            Nation_id integer,
            Description text,
            Secondary_DPM real,
            Hitting_DPM real,
            Range real,
            Reload text,
            Flight_time real,
            Horizontal_Dispertion real,
            Sigma real,
            Penetration text,
            Fire_chance text,
            Fire_per_minutes real,
            Shells_per_minutes real,
            foreign key (Tier_id) References Tier(id),
            foreign key (Class_id) references Class(id),
            foreign key (Nation_id) references Nation(id) 
)
""")

cur.execute ("""
Create table if not exists Sonar (
            id integer primary key autoincrement,
            Ship text,
            Tier_id integer,
            Class_id integer,
            Nation_id integer,
            Range real,
            Reload real,
            Turn_180 real,
            First_life_time real,
            Seconde_life_time real,
            Wave_width real,
            Wave_speed real,
            foreign key (Tier_id) References Tier(id),
            foreign key (Class_id) references Class(id),
            foreign key (Nation_id) references Nation(id) 
)
""")

cur.execute ("""
Create table if not exists Torpedoes (
            id integer primary key autoincrement,
            Ship text,
            Tier_id integer,
            Class_id integer,
            Nation_id integer,
            Description text,
            Type text,
            Loaders text,
            Torpedo_DPM real,
            Range real,
            Damage real,
            Spread text,
            Flood_chance real,
            Reload real,
            Speed real,
            Detectability real,
            Reaction_time real,
            Torpedoes_per_minutes real,
            Homming_rate real,
            foreign key (Tier_id) References Tier(id),
            foreign key (Class_id) references Class(id),
            foreign key (Nation_id) references Nation(id) 
)
""")

cur.execute ("""
Create table if not exists Anti_Aircraft (
            id integer primary key autoincrement,
            Ship text,
            Tier_id integer,
            Class_id integer,
            Nation_id integer,
            AA_strength integer,
            Long_range real,
            Long_DPS real,
            Medium_range real,
            Medium_DPS real,
            Short_range real,
            Short_DPS real,
            Flak_Strength real,
            Flak_count real,
            Flak_DPS real,
            Sector_time real,
            Sector_pourcentage real,
            DFAA_pourcentage real,
            foreign key (Tier_id) References Tier(id),
            foreign key (Class_id) references Class(id),
            foreign key (Nation_id) references Nation(id) 
)
""")

cur.execute ("""
Create table if not exists Deep_Charges (
            id integer primary key autoincrement,
            Ship text,
            Tier_id integer,
            Class_id intger,
            Nation_id integer,
            Attacks real,
            Reload real,
            Bombs real,
            Interval real,
            Detonation_timer text,
            Detonation_depth text,
            Damage real,
            Radius real,
            Flood_chance real,
            Fire_chance real,
            foreign key (Tier_id) References Tier(id),
            foreign key (Class_id) references Class(id),
            foreign key (Nation_id) references Nation(id)
)
""")

cur.execute("""
Create table if not exists Airstrike (
            id integer primary key autoincrement,
            Ship text,
            Tier_id integer,
            Class_id integer,
            Nation_id integer,
            Type text,
            Attacks real,
            Reload real,
            Min_distance real,
            Max_distance real,
            Bombs real,
            Retide_size text,
            Deto_timer text,
            Deto_depth text,
            Damage real,
            Radius real,
            Flood_chance real,
            Fire_chance real,
            Penetration real,
            foreign key (Tier_id) References Tier(id),
            foreign key (Class_id) references Class(id),
            foreign key (Nation_id) references Nation(id)
)
""")

cur.execute("""
Create table if not exists Attack_aircraft (
            id integer primary key autoincrement,
            Ship text,
            Tier_id integer,
            Class_id integer,
            Nation_id integer,
            Description text,
            Healt real,
            Max_speed real,
            Detectability real,
            On_Deck real,
            Regeneration text,
            Squadron text,
            Rockets real,
            Recticle_size text,
            Firing_dealy real,
            Type text,
            Damage real,
            Fire_chance real,
            Penetration real,
            Threshold real,
            Fuse_time real,
            foreign key (Tier_id) References Tier(id),
            foreign key (Class_id) references Class(id),
            foreign key (Nation_id) references Nation(id)
)
""")

cur.execute("""
Create table if not exists Torpedo_Bombers (
            id integer primary key autoincrement,
            Ship text,
            Tier_id integer,
            Class_id integer,
            Nation_id integer,
            Description text,
            Health real,
            Max_speed real,
            Detectability real,
            On_Deck real,
            Regeneration real,
            Squadron text,
            Torpedoes real,
            Tropedoes_speed real,
            Arming_time real,
            Arming_distance real,
            Range real,
            Damage real,
            Flood_chance real,
            foreign key (Tier_id) References Tier(id),
            foreign key (Class_id) references Class(id),
            foreign key (Nation_id) references Nation(id)
)
""")

cur.execute("""
Create table if not exists Bombers (
            id integer primary key autoincrement,
            Ship text,
            Tier_id integer,
            Class_id integer,
            Nation_id integer,
            Description text,
            Health real,
            Max_speed real,
            Detectability real,
            On_Deck real,
            Regeneration real,
            Squadron text,
            Bombs real,
            Reticl_size text,
            Type text,
            Damage real,
            Fire_chance real,
            Penetration real,
            Threshold real,
            Fuse_time real,
            foreign key (Tier_id) References Tier(id),
            foreign key (Class_id) references Class(id),
            foreign key (Nation_id) references Nation(id)
)
""")

cur.execute("""
Create table if not exists Skip_Bombers (
            id integer primary key autoincrement,
            Ship text,
            Tier_id integer,
            Class_id integer,
            Nation_id integer,
            Description text,
            Health real,
            Max_speed real,
            Detectability real,
            On_Deck real,
            Regeneration real,
            Squadron text,
            Bombs real,
            Type text,
            Damage real,
            Fire_chance real,
            Penetration real,
            Threshold real,
            Fuse_time real,
            foreign key (Tier_id) References Tier(id),
            foreign key (Class_id) references Class(id),
            foreign key (Nation_id) references Nation(id)
)
""")

# Enregistrement des modifications
con.commit()
con.close()