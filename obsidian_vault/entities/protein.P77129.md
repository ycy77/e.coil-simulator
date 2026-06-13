---
entity_id: "protein.P77129"
entity_type: "protein"
name: "allG"
source_database: "UniProt"
source_id: "P77129"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "allG ylbE b4572 b0519"
---

# allG

`protein.P77129`

## Static

- Type: `protein`
- Source: `UniProt:P77129`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of a carbamoyltransferase involved in the anaerobic nitrogen utilization via the assimilation of allantoin (PubMed:38888336). Catalyzes the conversion of oxalurate (N-carbamoyl-2-oxoglycine) to oxamate and carbamoyl phosphate (PubMed:38888336). {ECO:0000269|PubMed:38888336}. Resequencing of multiple isolates of the MG1655 strain has identified several genetic variations, including a single-nucleotide polymorphism and a single-nucleotide insertion in the former ylbE_1 pseudogene fragment in strain ATCC700926 , which is the source of the genome sequence within EcoCyc (U00096.3). This insertion repairs the frameshift and results in an intact ylbE gene . Using mutational analyses and purified proteins, this gene product, renamed AllG, was shown to be required for oxamate carbamoyltransferase (OXTCase) activity along with AllF and AllH subunits . The complex of three distinct subunits has not been observed for other enzymes of the transcarbamylase family in other organisms; also, the protein sequences for all three enzymes lack similarity to others in the transcarbamylase family . Expression of the ylbE ortholog of the avian pathogenic E. coli strain CH2 is induced during infection of chickens .

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

- `is_component_of` --> [[complex.ecocyc.CPLX0-12207|complex.ecocyc.CPLX0-12207]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4572|gene.b4572]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77129`
- `KEGG:eco:b4572;ecoc:C3026_02545;`
- `GeneID:4056025;75170542;`
- `GO:GO:0000256; GO:0050205`
- `EC:2.1.3.5`

## Notes

Oxamate carbamoyltransferase subunit AllG (OXTCase subunit AllG) (EC 2.1.3.5) (Oxamic transcarbamylase subunit AllG)
