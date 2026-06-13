---
entity_id: "molecule.C00031"
entity_type: "small_molecule"
name: "D-Glucose"
source_database: "KEGG"
source_id: "C00031"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Glucose"
  - "Grape sugar"
  - "Dextrose"
  - "Glucose"
  - "D-Glucopyranose"
  - "D-gluco-hexose"
---

# D-Glucose

`molecule.C00031`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00031`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Glucose; Grape sugar; Dextrose; Glucose; D-Glucopyranose EcoCyc common name: D-glucopyranose. This compound stands for a mixture of ALPHA-GLUCOSE and GLC. In most cases, each of these compounds mutarotates quickly to form a mixture of the two, and thus it is the general rule to use this non-specific form in reactions unless it is specifically known that an enzyme can accept only one of the forms.

## Biological Role

Consumed as substrate in 10 reaction(s). Produced in 33 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: D-Glucose; Grape sugar; Dextrose; Glucose; D-Glucopyranose

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (51)

- `is_product_of` --> [[reaction.R00010|reaction.R00010]] `KEGG` `database` - C01083 + C00001 <=> 2 C00031
- `is_product_of` --> [[reaction.R00028|reaction.R00028]] `KEGG` `database` - C00208 + C00001 <=> 2 C00031
- `is_product_of` --> [[reaction.R00304|reaction.R00304]] `KEGG` `database` - C00103 + C00001 <=> C00031 + C00009
- `is_product_of` --> [[reaction.R00306|reaction.R00306]] `KEGG` `database` - C00185 + C00001 <=> 2 C00031
- `is_product_of` --> [[reaction.R00801|reaction.R00801]] `KEGG` `database` - C00089 + C00001 <=> C00095 + C00031
- `is_product_of` --> [[reaction.R00837|reaction.R00837]] `KEGG` `database` - C00001 + C00689 <=> C00031 + C00092
- `is_product_of` --> [[reaction.R00839|reaction.R00839]] `KEGG` `database` - C04534 + C00001 <=> C00031 + C00092
- `is_product_of` --> [[reaction.R02887|reaction.R02887]] `KEGG` `database` - C01898 + (n-2) C00001 <=> (n-2) C00031 + C00185
- `is_product_of` --> [[reaction.R07264|reaction.R07264]] `KEGG` `database` - C15548 + C00009 <=> C00031 + C00663
- `is_product_of` --> [[reaction.ecocyc.2.4.1.230-RXN|reaction.ecocyc.2.4.1.230-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.3.2.1.21-RXN|reaction.ecocyc.3.2.1.21-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.6-PHOSPHO-BETA-GLUCOSIDASE-RXN|reaction.ecocyc.6-PHOSPHO-BETA-GLUCOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ALPHAGALACTOSID-RXN|reaction.ecocyc.ALPHAGALACTOSID-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.BETAGALACTOSID-RXN|reaction.ecocyc.BETAGALACTOSID-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GDP-GLUCOSIDASE-RXN|reaction.ecocyc.GDP-GLUCOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUCOSE-1-PHOSPHAT-RXN|reaction.ecocyc.GLUCOSE-1-PHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MALTODEG-RXN|reaction.ecocyc.MALTODEG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12402|reaction.ecocyc.RXN-12402]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14281|reaction.ecocyc.RXN-14281]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14408|reaction.ecocyc.RXN-14408]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14722|reaction.ecocyc.RXN-14722]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-17330|reaction.ecocyc.RXN-17330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-24170|reaction.ecocyc.RXN-24170]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5395|reaction.ecocyc.RXN0-5395]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6372|reaction.ecocyc.RXN0-6372]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6418|reaction.ecocyc.RXN0-6418]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7077|reaction.ecocyc.RXN0-7077]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7347|reaction.ecocyc.RXN0-7347]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7362|reaction.ecocyc.RXN0-7362]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN66-526|reaction.ecocyc.RXN66-526]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-320|reaction.ecocyc.TRANS-RXN-320]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-574|reaction.ecocyc.TRANS-RXN0-574]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRE6PHYDRO-RXN|reaction.ecocyc.TRE6PHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00299|reaction.R00299]] `KEGG` `database` - C00002 + C00031 <=> C00008 + C00092
- `is_substrate_of` --> [[reaction.ecocyc.AMYLOMALT-RXN|reaction.ecocyc.AMYLOMALT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLUCOKIN-RXN|reaction.ecocyc.GLUCOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14260|reaction.ecocyc.RXN-14260]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14261|reaction.ecocyc.RXN-14261]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6373|reaction.ecocyc.RXN0-6373]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7077|reaction.ecocyc.RXN0-7077]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-157|reaction.ecocyc.TRANS-RXN-157]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-320|reaction.ecocyc.TRANS-RXN-320]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-574|reaction.ecocyc.TRANS-RXN0-574]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.AMYLOMALT-RXN|reaction.ecocyc.AMYLOMALT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.MALTODEG-RXN|reaction.ecocyc.MALTODEG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-14260|reaction.ecocyc.RXN-14260]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-14261|reaction.ecocyc.RXN-14261]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-14722|reaction.ecocyc.RXN-14722]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-24169|reaction.ecocyc.RXN-24169]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-7347|reaction.ecocyc.RXN0-7347]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANS-RXN-30|reaction.ecocyc.TRANS-RXN-30]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0AEP1|protein.P0AEP1]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00031`
- `EcoCyc:D-Glucose`
- `CHEBI:17634`
- `canonicalized_from:molecule.ecocyc.D-Glucose`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.D-Glucose: EcoCyc:D-Glucose
