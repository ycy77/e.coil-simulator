---
entity_id: "molecule.C02528"
entity_type: "small_molecule"
name: "Chenodeoxycholate"
source_database: "KEGG"
source_id: "C02528"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Chenodeoxycholate"
  - "Chenodeoxycholic acid"
  - "3alpha,7alpha-Dihydroxy-5beta-cholanic acid"
  - "Chenodiol"
---

# Chenodeoxycholate

`molecule.C02528`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02528`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Chenodeoxycholate; Chenodeoxycholic acid; 3alpha,7alpha-Dihydroxy-5beta-cholanic acid; Chenodiol Bile (or gall) is a dark green to yellowish brown fluid, produced by the liver of most vertebrates, that aids the digestion of lipids in the small intestine. In humans bile is produced continuously by the liver and stored and concentrated in the gall bladder. After eating, the bile is discharged into the the first section of the small intestine (the duodenum). The main active ingredient (about 0.7%) of the bile is bile acids. Bile acids are classified into primary and secondary. The primary bile acids are produced in the liver from CHOLESTEROL. About half of the cholesterol produced in the body is used for bile acid synthesis. Their structures vary, as do their proportions in different species. The primary bile acids are conjugated in the liver with GLY or TAURINE before secretion into the bile. Further conversion into secondary bile acids occurs through the action of microbial enzymes in the gut. The primary bile acids CHOLATE and CPD-15189 are synthesized from CHOLESTEROL by a series of oxidative transformations in the liver. They are further modified by attachemnt of a glycine or taurine molecule, forming GLYCOCHOLIC_ACID, GLYCOCHENODEOXYCHOLIC_ACID, CPD-3743, and CPD-7283 (see PWY-6061)...

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00121` Secondary bile acid biosynthesis (KEGG)

## Annotation

KEGG compound: Chenodeoxycholate; Chenodeoxycholic acid; 3alpha,7alpha-Dihydroxy-5beta-cholanic acid; Chenodiol

## Pathways

- `eco00121` Secondary bile acid biosynthesis (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-591|reaction.ecocyc.TRANS-RXN0-591]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-592|reaction.ecocyc.TRANS-RXN0-592]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-591|reaction.ecocyc.TRANS-RXN0-591]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-592|reaction.ecocyc.TRANS-RXN0-592]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.TRANS-CPLX-201|complex.ecocyc.TRANS-CPLX-201]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C02528`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
