---
entity_id: "protein.P00963"
entity_type: "protein"
name: "asnA"
source_database: "UniProt"
source_id: "P00963"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "asnA b3744 JW3722"
---

# asnA

`protein.P00963`

## Static

- Type: `protein`
- Source: `UniProt:P00963`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: May amidate Asp of the extracellular death factor precursor Asn-Asn-Trp-Asp-Asn to generate Asn-Asn-Trp-Asn-Asn. {ECO:0000305|PubMed:17962566}.

## Biological Role

Catalyzes L-aspartate:ammonia ligase (AMP-forming) (reaction.R00483). Component of asparagine synthetase A (complex.ecocyc.ASNSYNA-CPLX).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: May amidate Asp of the extracellular death factor precursor Asn-Asn-Trp-Asp-Asn to generate Asn-Asn-Trp-Asn-Asn. {ECO:0000305|PubMed:17962566}.

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00483|reaction.R00483]] `KEGG` `database` - via EC:6.3.1.1
- `is_component_of` --> [[complex.ecocyc.ASNSYNA-CPLX|complex.ecocyc.ASNSYNA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3744|gene.b3744]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00963`
- `KEGG:ecj:JW3722;eco:b3744;ecoc:C3026_20285;`
- `GeneID:948258;`
- `GO:GO:0004071; GO:0005524; GO:0005829; GO:0006529; GO:0006974; GO:0042802; GO:0042803; GO:0070981`
- `EC:6.3.1.1`

## Notes

Aspartate--ammonia ligase (EC 6.3.1.1) (Asparagine synthetase A)
