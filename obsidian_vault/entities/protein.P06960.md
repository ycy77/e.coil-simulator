---
entity_id: "protein.P06960"
entity_type: "protein"
name: "argF"
source_database: "UniProt"
source_id: "P06960"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "argF b0273 JW0266"
---

# argF

`protein.P06960`

## Static

- Type: `protein`
- Source: `UniProt:P06960`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Reversibly catalyzes the transfer of the carbamoyl group from carbamoyl phosphate (CP) to the N(epsilon) atom of ornithine (ORN) to produce L-citrulline, which is a substrate for argininosuccinate synthetase, the enzyme involved in the final step in arginine biosynthesis. {ECO:0000269|PubMed:789338}.

## Biological Role

Component of ornithine carbamoyltransferase (complex.ecocyc.ORNCARBAMTRANSFERF-CPLX).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Reversibly catalyzes the transfer of the carbamoyl group from carbamoyl phosphate (CP) to the N(epsilon) atom of ornithine (ORN) to produce L-citrulline, which is a substrate for argininosuccinate synthetase, the enzyme involved in the final step in arginine biosynthesis. {ECO:0000269|PubMed:789338}.

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ORNCARBAMTRANSFERF-CPLX|complex.ecocyc.ORNCARBAMTRANSFERF-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0273|gene.b0273]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06960`
- `KEGG:ecj:JW0266;eco:b0273;ecoc:C3026_01325;`
- `GeneID:944844;`
- `GO:GO:0004585; GO:0005737; GO:0006974; GO:0016597; GO:0019240; GO:0042450; GO:0046872`
- `EC:2.1.3.3`

## Notes

Ornithine carbamoyltransferase subunit F (OTCase-2) (EC 2.1.3.3)
