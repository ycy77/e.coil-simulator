---
entity_id: "gene.b4326"
entity_type: "gene"
name: "iraD"
source_database: "NCBI RefSeq"
source_id: "gene-b4326"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4326"
  - "iraD"
---

# iraD

`gene.b4326`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4326`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

iraD (gene.b4326) is a gene entity. It encodes iraD (protein.P39375). Encoded protein function: FUNCTION: Inhibits RpoS proteolysis by regulating RssB activity, thereby increasing the stability of the sigma stress factor RpoS during oxidative stress. Its effect on RpoS stability is due to its interaction with RssB, which probably blocks the interaction of RssB with RpoS, and the consequent delivery of the RssB-RpoS complex to the ClpXP protein degradation pathway. {ECO:0000269|PubMed:18383615}. EcoCyc product frame: G7923-MONOMER. EcoCyc synonyms: yjiD. Genomic coordinates: 4556993-4557385. EcoCyc protein note: IraD is one of several small anti-adaptor proteins; it inhibits proteolysis of the stationary phase sigma factor RPOS-MONOMER σS by interacting with EG12121-MONOMER RssB, an adaptor protein that would normally target σS for degradation by the ClpXP protease . Each anti-adaptor protein interacts with RssB in a unique way . IraD is a major determinant of the steady-state level of RpoS . Increased expression of IraD and IraP contributes to the stabilization of σS in aceE mutants . A crystal structure of the RssB-IraD complex has been solved at 2 Å resolution; the data suggests that structural plasticity conferred by the flexible linker region between the N- and C-terminal domains of RssB is critical for its regulatory function...

## Biological Role

Repressed by dnaA (protein.P03004), lrp (protein.P0ACJ0), csrA (protein.P69913). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39375|protein.P39375]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=iraD; function=+
- `represses` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `C` - regulator=DnaA; target=iraD; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `S` - regulator=CsrA; target=iraD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014190,ECOCYC:G7923,GeneID:948851`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4556993-4557385:+; feature_type=gene
