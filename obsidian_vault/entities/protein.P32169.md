---
entity_id: "protein.P32169"
entity_type: "protein"
name: "rhaD"
source_database: "UniProt"
source_id: "P32169"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rhaD rhuA b3902 JW3873"
---

# rhaD

`protein.P32169`

## Static

- Type: `protein`
- Source: `UniProt:P32169`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the reversible cleavage of L-rhamnulose-1-phosphate to dihydroxyacetone phosphate (DHAP) and L-lactaldehyde (PubMed:12962479). Also catalyzes the dephosphorylation of phospho-serine in vitro (PubMed:25848029). {ECO:0000269|PubMed:12962479, ECO:0000269|PubMed:25848029}. Rhamnulose-1-phosphate aldolase is a class II aldolase that catalyzes the third step in the L-rhamnose degradation pathway. The enzyme contains 2 molecules of zinc per enzyme complex . If cobalt or selected other divalent metal ions are artificially substituted for zinc, the enzyme has an oxygenase activity in the presence of dihydroxyacetone phosphate . The enzyme has been crystallized , and crystal structures have been solved . A catalytic mechanism was proposed based on results from site-directed mutagenesis in combination with structural information . Anisotropic mobility of the N-terminal "antenna domain" supports catalysis . Stereospecificity of RhaD has been investigated . For the aldol addition reaction, RhaD accepts a range of aldehydes in place of L-lactaldehyde; this property has been used for synthesis of a variety of compounds of interest . RhaD (there called Rua) was used in a study of designed protein-protein associations; certain mutations generated a new contact surface and allowed formation of an octamer . Expression of RhaD is induced by L-rhamnose as well as L-lyxose...

## Biological Role

Component of rhamnulose-1-phosphate aldolase (complex.ecocyc.RHAMNULPALDOL-CPLX).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible cleavage of L-rhamnulose-1-phosphate to dihydroxyacetone phosphate (DHAP) and L-lactaldehyde (PubMed:12962479). Also catalyzes the dephosphorylation of phospho-serine in vitro (PubMed:25848029). {ECO:0000269|PubMed:12962479, ECO:0000269|PubMed:25848029}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.RHAMNULPALDOL-CPLX|complex.ecocyc.RHAMNULPALDOL-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3902|gene.b3902]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32169`
- `KEGG:ecj:JW3873;eco:b3902;ecoc:C3026_21095;`
- `GeneID:948401;`
- `GO:GO:0005829; GO:0008994; GO:0016832; GO:0019301; GO:0019323; GO:0042802; GO:0046872`
- `EC:4.1.2.19`

## Notes

Rhamnulose-1-phosphate aldolase (EC 4.1.2.19)
