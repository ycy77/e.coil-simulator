---
entity_id: "protein.P0A890"
entity_type: "protein"
name: "tusA"
source_database: "UniProt"
source_id: "P0A890"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00413, ECO:0000269|PubMed:10830496}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tusA sirA yhhP b3470 JW3435"
---

# tusA

`protein.P0A890`

## Static

- Type: `protein`
- Source: `UniProt:P0A890`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00413, ECO:0000269|PubMed:10830496}.

## Enriched Summary

FUNCTION: Sulfur carrier protein involved in sulfur trafficking in the cell. Part of a sulfur-relay system required for 2-thiolation during synthesis of 2-thiouridine of the modified wobble base 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) in tRNA (PubMed:16387657). Interacts with IscS and stimulates its cysteine desulfurase activity (PubMed:16387657, PubMed:23281480). Accepts an activated sulfur from IscS, which is then transferred to TusD, and thus determines the direction of sulfur flow from IscS to 2-thiouridine formation (PubMed:16387657). Also appears to be involved in sulfur transfer for the biosynthesis of molybdopterin (PubMed:23281480). Seems to affect the stability of sigma-S, particularly during the logarithmic growth phase (PubMed:9555915). {ECO:0000269|PubMed:16387657, ECO:0000269|PubMed:23281480, ECO:0000269|PubMed:9555915}. TusA has pleiotrophic roles in thiomodification of some tRNAs, sulfur transfer in molybdenum cofactor biosynthesis, general Fe-S cluster assembly, and iron homeostasis. It functions as a sulfur mediator during tRNA synthesis of 2-thiouridine of the modified wobble base mnm5s2U in tRNA by interacting with CPLX0-248, stimulating its cysteine desulfurase activity and accepting an activated sulfur in the form of a persulfide at the cysteine residue C19...

## Biological Role

Catalyzes RXN-12473 (reaction.ecocyc.RXN-12473), RXN-18709 (reaction.ecocyc.RXN-18709). Component of IscS:TusA sulfurtransferase (complex.ecocyc.CPLX0-12610).

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: Sulfur carrier protein involved in sulfur trafficking in the cell. Part of a sulfur-relay system required for 2-thiolation during synthesis of 2-thiouridine of the modified wobble base 5-methylaminomethyl-2-thiouridine (mnm(5)s(2)U) in tRNA (PubMed:16387657). Interacts with IscS and stimulates its cysteine desulfurase activity (PubMed:16387657, PubMed:23281480). Accepts an activated sulfur from IscS, which is then transferred to TusD, and thus determines the direction of sulfur flow from IscS to 2-thiouridine formation (PubMed:16387657). Also appears to be involved in sulfur transfer for the biosynthesis of molybdopterin (PubMed:23281480). Seems to affect the stability of sigma-S, particularly during the logarithmic growth phase (PubMed:9555915). {ECO:0000269|PubMed:16387657, ECO:0000269|PubMed:23281480, ECO:0000269|PubMed:9555915}.

## Pathways

- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-12473|reaction.ecocyc.RXN-12473]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-18709|reaction.ecocyc.RXN-18709]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-12610|complex.ecocyc.CPLX0-12610]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3470|gene.b3470]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A890`
- `KEGG:ecj:JW3435;eco:b3470;ecoc:C3026_18795;`
- `GeneID:86862134;93778521;947974;`
- `GO:GO:0002143; GO:0005829; GO:0006777; GO:0016226; GO:0019448; GO:0097163; GO:1990329`

## Notes

Sulfur carrier protein TusA (Sulfur mediator TusA) (Sulfur transfer protein TusA) (tRNA 2-thiouridine synthesizing protein A)
