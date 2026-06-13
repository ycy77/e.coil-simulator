---
entity_id: "reaction.ecocyc.THREDEHYD-RXN"
entity_type: "reaction"
name: "THREDEHYD-RXN"
source_database: "EcoCyc"
source_id: "THREDEHYD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Serine deaminase"
  - "L-serine dehydratase"
  - "Threonine deaminase"
---

# THREDEHYD-RXN

`reaction.ecocyc.THREDEHYD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THREDEHYD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first step in isoleucine biosynthesis and threonine catabolism. The reaction catalyzed probably involves initial elimination of water (hence the enzyme's original classification as EC 4.2.1.16), followed by isomerization and hydrolysis of the product with C-N bond breakage. The enzymes isolated from a number of sources can also act on L-serine (EC# 4.3.1.17). This reaction was formerly classified as EC 4.2.1.16. While enzymes purified from most organisms require pyridoxal-phosphate, some enzymes, such as the one isolated from P. putida do not require it. EcoCyc reaction equation: THR -> 2-OXOBUTANOATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first step in isoleucine biosynthesis and threonine catabolism. The reaction catalyzed probably involves initial elimination of water (hence the enzyme's original classification as EC 4.2.1.16), followed by isomerization and hydrolysis of the product with C-N bond breakage. The enzymes isolated from a number of sources can also act on L-serine (EC# 4.3.1.17). This reaction was formerly classified as EC 4.2.1.16. While enzymes purified from most organisms require pyridoxal-phosphate, some enzymes, such as the one isolated from P. putida do not require it.

## Biological Role

Catalyzed by catabolic threonine dehydratase (complex.ecocyc.THREDEHYDCAT-CPLX), threonine deaminase (complex.ecocyc.THREDEHYDSYN-CPLX). Substrates: L-Threonine (molecule.C00188). Products: 2-Oxobutanoate (molecule.C00109), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

This is the first step in isoleucine biosynthesis and threonine catabolism. The reaction catalyzed probably involves initial elimination of water (hence the enzyme's original classification as EC 4.2.1.16), followed by isomerization and hydrolysis of the product with C-N bond breakage. The enzymes isolated from a number of sources can also act on L-serine (EC# 4.3.1.17). This reaction was formerly classified as EC 4.2.1.16. While enzymes purified from most organisms require pyridoxal-phosphate, some enzymes, such as the one isolated from P. putida do not require it.

## Outgoing Edges (0)

_None._

## Incoming Edges (18)

- `activates` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.THREDEHYDCAT-CPLX|complex.ecocyc.THREDEHYDCAT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.THREDEHYDSYN-CPLX|complex.ecocyc.THREDEHYDSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00109|molecule.C00109]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00109|molecule.C00109]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00407|molecule.C00407]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00740|molecule.C00740]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00793|molecule.C00793]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00820|molecule.C00820]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.2-Oxo-Acids|molecule.ecocyc.2-Oxo-Acids]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1234|molecule.ecocyc.CPD0-1234]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:THREDEHYD-RXN`

## Notes

THR -> 2-OXOBUTANOATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT
