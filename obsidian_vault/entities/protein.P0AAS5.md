---
entity_id: "protein.P0AAS5"
entity_type: "protein"
name: "allH"
source_database: "UniProt"
source_id: "P0AAS5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "allH ylbF b0520 JW0509"
---

# allH

`protein.P0AAS5`

## Static

- Type: `protein`
- Source: `UniProt:P0AAS5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of a carbamoyltransferase involved in the anaerobic nitrogen utilization via the assimilation of allantoin (PubMed:38888336). Catalyzes the conversion of oxalurate (N-carbamoyl-2-oxoglycine) to oxamate and carbamoyl phosphate (PubMed:38888336). {ECO:0000269|PubMed:38888336}. Using genome and metabolic context methods, ylbF is predicted to encode an oxamate carbamoyltransferase that is active in the PWY0-41 "anaerobic allantoin degradation pathway" . Using mutational analyses and purified proteins, this gene product, renamed AllH, was shown to be required for oxamate carbamoyltransferase (OXTCase) activity along with AllF and AllG subunits . The complex of three distinct subunits has not been observed for other enzymes of the transcarbamylase family in other organisms; also, the protein sequences for all three enzymes lack similarity to others in the transcarbamylase family .

## Biological Role

Component of oxamate carbamoyltransferase (complex.ecocyc.CPLX0-12207).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Component of a carbamoyltransferase involved in the anaerobic nitrogen utilization via the assimilation of allantoin (PubMed:38888336). Catalyzes the conversion of oxalurate (N-carbamoyl-2-oxoglycine) to oxamate and carbamoyl phosphate (PubMed:38888336). {ECO:0000269|PubMed:38888336}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-12207|complex.ecocyc.CPLX0-12207]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0520|gene.b0520]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAS5`
- `KEGG:ecj:JW0509;eco:b0520;ecoc:C3026_02550;`
- `GeneID:945195;`
- `GO:GO:0000256; GO:0050205`
- `EC:2.1.3.5`

## Notes

Oxamate carbamoyltransferase subunit AllH (OXTCase subunit AllH) (EC 2.1.3.5) (Oxamic transcarbamylase subunit AllH)
