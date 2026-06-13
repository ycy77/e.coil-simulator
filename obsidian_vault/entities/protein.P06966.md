---
entity_id: "protein.P06966"
entity_type: "protein"
name: "dicA"
source_database: "UniProt"
source_id: "P06966"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dicA b1570 JW1562"
---

# dicA

`protein.P06966`

## Static

- Type: `protein`
- Source: `UniProt:P06966`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein is a repressor of division inhibition gene dicB. The transcription factor DicA, "Division control," is a temperature-sensitive repressor that controls the transcription of genes involved in the cell division process and activation of its own expression . Nevertheless, the signal to which DicA responds is still unknown. The family to which DicA belongs has not been established; it is a protein of 15 kDa with a hypothetical DNA-binding domain in the N-terminal domain . DicA is homologous in structure and function to RovA (Yersinia) and SlyA (Salmonella), both of which are activators for pathogenicity-related genes . Rem has been identified as a putative antirepressor of DicA, encoded in the cryptic prophage Qin, as it induces the derepression of dicBp, a promoter repressed by DicA . A dicA hypomorphic allele mutant strain had growth defects and long filamentation, and this phenotype was rescued to near-wild-type when the gene encoding the TF YjdC (DicD) was deleted. In a dicA hypomorphic allele mutant strain, the TF YjdC is transcriptionally downregulated . The DicA binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data...

## Annotation

FUNCTION: This protein is a repressor of division inhibition gene dicB.

## Outgoing Edges (4)

- `activates` --> [[gene.b1570|gene.b1570]] `RegulonDB` `S` - regulator=DicA; target=dicA; function=+
- `represses` --> [[gene.b1567|gene.b1567]] `RegulonDB` `S` - regulator=DicA; target=ydfW; function=-
- `represses` --> [[gene.b1568|gene.b1568]] `RegulonDB` `S` - regulator=DicA; target=ydfX; function=-
- `represses` --> [[gene.b1569|gene.b1569]] `RegulonDB` `S` - regulator=DicA; target=dicC; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1570|gene.b1570]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06966`
- `KEGG:ecj:JW1562;eco:b1570;ecoc:C3026_09050;`
- `GeneID:946241;`
- `GO:GO:0003677; GO:0006351; GO:0051301`

## Notes

HTH-type transcriptional regulator DicA (Repressor protein of division inhibition gene dicA)
