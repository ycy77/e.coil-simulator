---
entity_id: "gene.b1569"
entity_type: "gene"
name: "dicC"
source_database: "NCBI RefSeq"
source_id: "gene-b1569"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1569"
  - "dicC"
---

# dicC

`gene.b1569`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1569`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dicC (gene.b1569) is a gene entity. It encodes dicC (protein.P06965). Encoded protein function: FUNCTION: This protein is a repressor of division inhibition gene dicB. EcoCyc product frame: EG10228-MONOMER. EcoCyc synonyms: ftsT. Genomic coordinates: 1647620-1647850. EcoCyc protein note: DicC has similarity to the bacteriophage P22 Cro transcriptional regulator. The organization of the dicAC locus is similar to the P22 immunity region. In the dicA1 mutant, expression of the dicAC locus appears to be under the control of DicC . Overexpression of dicC from a multicopy plasmid can complement the cell division phenotype of the dicA1 mutant . Expression of dicC is repressed by DicA . The DicC binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu . DicC: "division control C"

## Biological Role

Repressed by dicA (protein.P06966), yjdC (protein.P0ACU7). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06965|protein.P06965]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dicC; function=+
- `represses` <-- [[protein.P06966|protein.P06966]] `RegulonDB` `S` - regulator=DicA; target=dicC; function=-
- `represses` <-- [[protein.P0ACU7|protein.P0ACU7]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005244,ECOCYC:EG10228,GeneID:946120`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1647620-1647850:-; feature_type=gene
