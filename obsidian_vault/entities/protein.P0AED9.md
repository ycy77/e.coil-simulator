---
entity_id: "protein.P0AED9"
entity_type: "protein"
name: "dcm"
source_database: "UniProt"
source_id: "P0AED9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dcm mec b1961 JW1944"
---

# dcm

`protein.P0AED9`

## Static

- Type: `protein`
- Source: `UniProt:P0AED9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This methylase recognizes the double-stranded sequence 5'-CCWGG-3', methylates C-2 on both strands. {ECO:0000303|PubMed:12654995, ECO:0000305|PubMed:2198248}. Dcm is a DNA cytosine methyltransferase that preferentially methylates sites of sequence 5' C-MeC-T 3' . This modification interferes with cleavage by the EcoRII restriction enzyme , but does not offer the cell full protection from EcoRII . Not all Dcm methylation sites are modified in vivo . The reaction catalyzed by Dcm has been characterized . Methylated cytosines are subject to deamination, which causes mutation of the C to a T, and Dcm and the product of the adjacent gene, Vsr, are associated with a corrective mismatch repair activity, very short patch (VSP) repair . Dcm has also affects transposition by Tn3 . Dcm is non-essential; a dcm mutant is viable . Dcm also has utility as a modification enzyme that interferes with cleavage by several restriction enzymes used in the molecular biology laboratory . Regulation has been described . Dcm: "DNA cytosine methylase" Mec: "5-methyl-cytosine" Reviews:

## Biological Role

Catalyzes S-adenosyl-L-methionine:DNA (cytosine-5-)-methyltransferase (reaction.R00380), DNA-CYTOSINE-5--METHYLTRANSFERASE-RXN (reaction.ecocyc.DNA-CYTOSINE-5--METHYLTRANSFERASE-RXN).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: This methylase recognizes the double-stranded sequence 5'-CCWGG-3', methylates C-2 on both strands. {ECO:0000303|PubMed:12654995, ECO:0000305|PubMed:2198248}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00380|reaction.R00380]] `KEGG` `database` - via EC:2.1.1.37
- `catalyzes` --> [[reaction.ecocyc.DNA-CYTOSINE-5--METHYLTRANSFERASE-RXN|reaction.ecocyc.DNA-CYTOSINE-5--METHYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1961|gene.b1961]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AED9`
- `KEGG:ecj:JW1944;eco:b1961;ecoc:C3026_11090;`
- `GeneID:86946876;946479;`
- `GO:GO:0003677; GO:0003886; GO:0009307; GO:0032259; GO:0044027`
- `EC:2.1.1.37`

## Notes

DNA-cytosine methyltransferase (EC 2.1.1.37) (Type II methyltransferase M.EcoKDcm) (M.EcoKDcm)
