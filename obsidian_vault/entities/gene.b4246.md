---
entity_id: "gene.b4246"
entity_type: "gene"
name: "pyrL"
source_database: "NCBI RefSeq"
source_id: "gene-b4246"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4246"
  - "pyrL"
---

# pyrL

`gene.b4246`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4246`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pyrL (gene.b4246) is a gene entity. It encodes pyrL (protein.P0AD83). Encoded protein function: pyr operon leader peptide (pyrBI operon attenuator) EcoCyc product frame: EG11279-MONOMER. EcoCyc synonyms: pyrE-, pyrE-LP. Genomic coordinates: 4472399-4472533. EcoCyc protein note: The PyrL leader peptide is involved in the control by attenuation of the expression of the pyrLBI operon . Within the pyrL sequence there is a poly-T tract that leads to polymerase pausing when UTP is not available. This pausing lets the ribosome that is translating the leader peptide sequence catch up to the polymerase, preventing formation of a terminator that blocks transcription of the rest of the operon. When UTP is abundant, the polymerase moves through the pause site and outpaces the ribosome, leading to premature termination. . For more information on this means of regulation, look at the entry for TU00484. Although pyrimidine levels have little effect on translation of PyrL, translation of the leader peptide is required for proper regulation by attenuation. Mutations that block translation of PyrL disrupt attenuation at pyrLBI .

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD83|protein.P0AD83]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=pyrL; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=pyrL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013899,ECOCYC:EG11279,GeneID:948768`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4472399-4472533:-; feature_type=gene
