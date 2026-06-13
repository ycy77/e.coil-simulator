---
entity_id: "protein.P0A761"
entity_type: "protein"
name: "nanE"
source_database: "UniProt"
source_id: "P0A761"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nanE yhcJ b3223 JW3192"
---

# nanE

`protein.P0A761`

## Static

- Type: `protein`
- Source: `UniProt:P0A761`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Converts N-acetylmannosamine-6-phosphate (ManNAc-6-P) to N-acetylglucosamine-6-phosphate (GlcNAc-6-P). {ECO:0000305}. NanE is predicted to encode N-acetylmannosamine-6-phosphate 2-epimerase, an enzyme involved in the utilization of N-acetylneuraminate and N-acetylmannosamine as carbon sources . NanE from the pathogenic E. coli strain K1 has been purified and assayed . NanE can act as an allosteric activator of GLUCOSAMINE-6-P-DEAMIN-MONOMER . A protein with N-acetylmannosamine-6-phosphate epimerase activity was purified from E. coli K92; its molecular weight is 38.4 kDa, and its sequence was highly similar to pgl, but not nanE . Transcription of the nanATEKQ (sialic acid catabolic) operon is repressed by NanR . Expression of nanE is necessary for growth on ManNAc in an mlc mutant background . A nanE mutant is unable to utilize N-acetylneuraminate or N-glycolylneuraminate as the sole carbon source . A nanE mutant strain shows enhanced ethanol and hydrogen production when grown anaerobically in LB-glycerol...

## Biological Role

Catalyzes N-acetyl-D-mannosamine-6-phosphate epimerase (reaction.ecocyc.NANE-RXN).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Converts N-acetylmannosamine-6-phosphate (ManNAc-6-P) to N-acetylglucosamine-6-phosphate (GlcNAc-6-P). {ECO:0000305}.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `activates` --> [[reaction.ecocyc.GLUCOSAMINE-6-P-DEAMIN-RXN|reaction.ecocyc.GLUCOSAMINE-6-P-DEAMIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` --> [[reaction.ecocyc.NANE-RXN|reaction.ecocyc.NANE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3223|gene.b3223]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A761`
- `KEGG:ecj:JW3192;eco:b3223;ecoc:C3026_17535;`
- `GeneID:75206073;947745;`
- `GO:GO:0005829; GO:0005975; GO:0006053; GO:0019262; GO:0047465`
- `EC:5.1.3.9`

## Notes

Putative N-acetylmannosamine-6-phosphate 2-epimerase (EC 5.1.3.9) (ManNAc-6-P epimerase)
