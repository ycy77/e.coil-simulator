---
entity_id: "protein.P04391"
entity_type: "protein"
name: "argI"
source_database: "UniProt"
source_id: "P04391"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "argI b4254 JW4211"
---

# argI

`protein.P04391`

## Static

- Type: `protein`
- Source: `UniProt:P04391`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Reversibly catalyzes the transfer of the carbamoyl group from carbamoyl phosphate (CP) to the N(epsilon) atom of ornithine (ORN) to produce L-citrulline, which is a substrate for argininosuccinate synthetase, the enzyme involved in the final step in arginine biosynthesis. {ECO:0000269|PubMed:3072022, ECO:0000269|PubMed:789338}.

## Biological Role

Component of ornithine carbamoyltransferase (complex.ecocyc.ORNCARBAMTRANSFERI-CPLX).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Reversibly catalyzes the transfer of the carbamoyl group from carbamoyl phosphate (CP) to the N(epsilon) atom of ornithine (ORN) to produce L-citrulline, which is a substrate for argininosuccinate synthetase, the enzyme involved in the final step in arginine biosynthesis. {ECO:0000269|PubMed:3072022, ECO:0000269|PubMed:789338}.

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ORNCARBAMTRANSFERI-CPLX|complex.ecocyc.ORNCARBAMTRANSFERI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b4254|gene.b4254]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04391`
- `KEGG:ecj:JW4211;eco:b4254;ecoc:C3026_22950;`
- `GeneID:948774;`
- `GO:GO:0004585; GO:0005737; GO:0016597; GO:0019240; GO:0042450; GO:0046872`
- `EC:2.1.3.3`

## Notes

Ornithine carbamoyltransferase subunit I (OTCase-1) (EC 2.1.3.3)
