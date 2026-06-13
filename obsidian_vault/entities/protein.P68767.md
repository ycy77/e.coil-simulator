---
entity_id: "protein.P68767"
entity_type: "protein"
name: "pepA"
source_database: "UniProt"
source_id: "P68767"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pepA carP xerB b4260 JW4217"
---

# pepA

`protein.P68767`

## Static

- Type: `protein`
- Source: `UniProt:P68767`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probably involved in the processing and regular turnover of intracellular proteins (PubMed:20067529). Catalyzes the removal of unsubstituted N-terminal amino acids from various peptides. Required for plasmid ColE1 site-specific recombination but not in its aminopeptidase activity. Could act as a structural component of the putative nucleoprotein complex in which the Xer recombination reaction takes place (PubMed:8057849). {ECO:0000269|PubMed:8057849, ECO:0000305|PubMed:20067529}.

## Biological Role

Component of aminopeptidase A/I and DNA-binding transcriptional repressor PepA (complex.ecocyc.CPLX0-3061).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Probably involved in the processing and regular turnover of intracellular proteins (PubMed:20067529). Catalyzes the removal of unsubstituted N-terminal amino acids from various peptides. Required for plasmid ColE1 site-specific recombination but not in its aminopeptidase activity. Could act as a structural component of the putative nucleoprotein complex in which the Xer recombination reaction takes place (PubMed:8057849). {ECO:0000269|PubMed:8057849, ECO:0000305|PubMed:20067529}.

## Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3061|complex.ecocyc.CPLX0-3061]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `represses` --> [[gene.b0032|gene.b0032]] `RegulonDB` `S` - regulator=PepA; target=carA; function=-
- `represses` --> [[gene.b0033|gene.b0033]] `RegulonDB` `S` - regulator=PepA; target=carB; function=-
- `represses` --> [[gene.b4260|gene.b4260]] `RegulonDB` `S` - regulator=PepA; target=pepA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4260|gene.b4260]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P68767`
- `KEGG:ecj:JW4217;eco:b4260;ecoc:C3026_22980;`
- `GeneID:86861346;93777558;948791;`
- `GO:GO:0001073; GO:0003677; GO:0004177; GO:0005737; GO:0006276; GO:0006351; GO:0006508; GO:0030145; GO:0042150; GO:0043171; GO:0070006`
- `EC:3.4.11.1; 3.4.11.10`

## Notes

Cytosol aminopeptidase (EC 3.4.11.1) (Aminopeptidase A/I) (Leucine aminopeptidase) (LAP) (EC 3.4.11.10) (Leucyl aminopeptidase)
