---
entity_id: "gene.b0584"
entity_type: "gene"
name: "fepA"
source_database: "NCBI RefSeq"
source_id: "gene-b0584"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0584"
  - "fepA"
---

# fepA

`gene.b0584`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0584`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fepA (gene.b0584) is a gene entity. It encodes fepA (protein.P05825). Encoded protein function: FUNCTION: This protein is involved in the initial step of iron uptake by binding ferrienterobactin (Fe-ENT), an iron chelatin siderophore that allows E.coli to extract iron from the environment. FepA also acts as a receptor for colicins B and D. EcoCyc product frame: EG10293-MONOMER. EcoCyc synonyms: cbr, cbt, fep, feuB. Genomic coordinates: 610254-612494. EcoCyc protein note: FepA is an outer membrane (OM) protein that binds and transports ferric enterobactin (ferric enterochelin) ; it also binds and transports colicins B and D ( and reviewed in ). FepA mediated transport across the OM is energised by the inner membrane proton gradient; energy transduction is facilitated by the CPLX0-1923 (reviewed in ). FepA transports ferric enterobactin and its degradation products, CPD-21612 Fe(DHBS)2 and ferric dihydroxybenzoate (FeDHBA3) . FepA is a gated outer membrane porin . FepA is a 22-strand antiparallel β-barrel with an N-terminal globular domain which folds into the barrel plugging the pore. The structure contains several extracellular loops that would extend beyond the OM bilayer and may be involved ferric enterobactin binding . A 'ball and chain' mechanism of transport for FepA, in which the globular domain moves in and out of the channel to facilitate transport, has been proposed...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), omrA (gene.b4444), omrB (gene.b4445), fur (protein.P0A9A9). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05825|protein.P05825]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fepA; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4444|gene.b4444]] `RegulonDB` `S` - regulator=OmrA; target=fepA; function=-
- `represses` <-- [[gene.b4445|gene.b4445]] `RegulonDB` `S` - regulator=OmrB; target=fepA; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=fepA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002014,ECOCYC:EG10293,GeneID:945193`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:610254-612494:-; feature_type=gene
