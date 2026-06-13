---
entity_id: "gene.b3742"
entity_type: "gene"
name: "mioC"
source_database: "NCBI RefSeq"
source_id: "gene-b3742"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3742"
  - "mioC"
---

# mioC

`gene.b3742`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3742`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mioC (gene.b3742) is a gene entity. It encodes mioC (protein.P03817). Encoded protein function: FUNCTION: Probable electron transporter required for biotin synthase activity. EcoCyc product frame: EG11199-MONOMER. EcoCyc synonyms: yieB. Genomic coordinates: 3926012-3926455. EcoCyc protein note: MioC is an FMN binding protein that is involved in regulating cell division . In an in vitro system, MioC was found to be required for activity of biotin synthase . However, a mioC mutant does not require biotin for growth (D. Bates, unpublished observation noted in ). MioC, the protein, is not required for wild-type DNA replication at oriC , but was later found to promote cell division . MioC has similarity to flavodoxin family proteins ; its structure was predicted to exhibit an α/β twisted open-sheet fold . Solution structures of the apo- and holo forms of MioC have been solved, confirming the flavodoxin-like α/β sandwich structure. FMN binding induces structural stabilization . Mutations in mioC do not cause defects in cell growth or size, in the amount of DNA or number of origins of DNA replication measured per cell, or in timing of oriC replication initiation . A promoter mutation that blocks transcription of mioC results in cells that are 35% longer than wild type, but has no effect on DNA replication and chromosome segregation...

## Biological Role

Repressed by mraZ (protein.P22186), nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03817|protein.P03817]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mioC; function=+
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `S` - regulator=MraZ; target=mioC; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=mioC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012235,ECOCYC:EG11199,GeneID:948249`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3926012-3926455:-; feature_type=gene
