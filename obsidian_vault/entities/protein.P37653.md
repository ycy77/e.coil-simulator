---
entity_id: "protein.P37653"
entity_type: "protein"
name: "bcsA"
source_database: "UniProt"
source_id: "P37653"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bcsA yhjO yhjP b3533 JW5665"
---

# bcsA

`protein.P37653`

## Static

- Type: `protein`
- Source: `UniProt:P37653`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalytic subunit of cellulose synthase. It polymerizes uridine 5'-diphosphate glucose to cellulose, which is produced as an extracellular component for mechanical and chemical protection at the onset of the stationary phase, when the cells exhibit multicellular behavior (rdar morphotype). Coexpression of cellulose and thin aggregative fimbriae (curli fimbrae or fibers) leads to a hydrophobic network with tightly packed cells embedded in a highly inert matrix that confers cohesion, elasticity and tissue-like properties to colonies (PubMed:24097954). {ECO:0000269|PubMed:11260463, ECO:0000269|PubMed:24097954}. bcsA has sequence similarity to the gene encoding the catalytic subunit of cellulose synthase from the model cellulose producing organism Acetobacter xylinus ; the protein contains a conserved C-terminal PilZ c-di-GMP binding domain . In E. coli K-12 strains such as W3110 and MG1655, a "domesticating SNP" consists of a point mutation that introduces a stop codon after the first 5 amino acids of the wild-type bcsQ ORF. This domesticating SNP lowers expression of both bcsQ and the downstream bcsA gene. After repairing the SNP, the resulting "de-domesticated" W3110 derivative strain produces cellulose and has dramatically altered biofilm morphology. A ΔbcsA mutation introduced into this strain leads to loss of cellulose biosynthesis (see also )...

## Biological Role

Catalyzes UDPglucose:1,4-beta-D-glucan 4-beta-D-glucosyltransferase (reaction.R02889). Component of cellulose synthase (complex.ecocyc.CPLX0-8125).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Catalytic subunit of cellulose synthase. It polymerizes uridine 5'-diphosphate glucose to cellulose, which is produced as an extracellular component for mechanical and chemical protection at the onset of the stationary phase, when the cells exhibit multicellular behavior (rdar morphotype). Coexpression of cellulose and thin aggregative fimbriae (curli fimbrae or fibers) leads to a hydrophobic network with tightly packed cells embedded in a highly inert matrix that confers cohesion, elasticity and tissue-like properties to colonies (PubMed:24097954). {ECO:0000269|PubMed:11260463, ECO:0000269|PubMed:24097954}.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R02889|reaction.R02889]] `KEGG` `database` - via EC:2.4.1.12
- `is_component_of` --> [[complex.ecocyc.CPLX0-8125|complex.ecocyc.CPLX0-8125]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3533|gene.b3533]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37653`
- `KEGG:ecj:JW5665;eco:b3533;ecoc:C3026_19140;`
- `GeneID:75173723;948053;`
- `GO:GO:0005886; GO:0006011; GO:0016758; GO:0016760; GO:0030244; GO:0035438; GO:0090540`
- `EC:2.4.1.12`

## Notes

Cellulose synthase catalytic subunit [UDP-forming] (EC 2.4.1.12)
