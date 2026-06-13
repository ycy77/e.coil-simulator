---
entity_id: "gene.b0176"
entity_type: "gene"
name: "rseP"
source_database: "NCBI RefSeq"
source_id: "gene-b0176"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0176"
  - "rseP"
---

# rseP

`gene.b0176`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0176`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rseP (gene.b0176) is a gene entity. It encodes rseP (protein.P0AEH1). Encoded protein function: FUNCTION: A site-2 regulated intramembrane protease (S2P) that cleaves the peptide bond between 'Ala-108' and 'Cys-109' in the transmembrane region of RseA. Part of a regulated intramembrane proteolysis (RIP) cascade. Acts on DegS-cleaved RseA to release the cytoplasmic domain of RseA, residue 'Val-148' of RseA may be required for this. This provides the cell with sigma-E (RpoE) activity through the proteolysis of RseA. Can also cleave sequences in transmembrane regions of other proteins (such as LacY) as well as liberated signal peptides of beta-lactamase, OmpF, LivK, SecM, PhoA, LivJ, OmpC, Lpp and TorA, probably within the membrane. Cleaves FecR within its transmembrane region to release an N-terminal cytoplasmic fragment which binds to sigma factor FecI, allowing it to activate transcription of the fecABCDE operon which mediates ferric citrate transport (PubMed:33865858). {ECO:0000269|PubMed:12183368, ECO:0000269|PubMed:12183369, ECO:0000269|PubMed:15496982, ECO:0000269|PubMed:18268014, ECO:0000269|PubMed:18945679, ECO:0000269|PubMed:21810987, ECO:0000269|PubMed:33865858}. EcoCyc product frame: EG12436-MONOMER. EcoCyc synonyms: ecfE, yaeL. Genomic coordinates: 196546-197898...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEH1|protein.P0AEH1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rseP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000603,ECOCYC:EG12436,GeneID:944871`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:196546-197898:+; feature_type=gene
