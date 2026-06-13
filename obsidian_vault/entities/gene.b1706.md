---
entity_id: "gene.b1706"
entity_type: "gene"
name: "selO"
source_database: "NCBI RefSeq"
source_id: "gene-b1706"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1706"
  - "selO"
---

# selO

`gene.b1706`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1706`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

selO (gene.b1706) is a gene entity. It encodes selO (protein.P77649). Encoded protein function: FUNCTION: Nucleotidyltransferase involved in the post-translational modification of proteins (PubMed:30270044, PubMed:32966796, PubMed:35532215, PubMed:35532216). It can catalyze the addition of adenosine monophosphate (AMP) or uridine monophosphate (UMP) to a protein, resulting in modifications known as AMPylation and UMPylation (PubMed:30270044, PubMed:32966796, PubMed:35532215, PubMed:35532216). It could be involved in stress resistance and play a crucial role in regulating essential bacterial processes, including flagella synthesis and iron uptake (PubMed:32966796, PubMed:35532215, PubMed:35532216). {ECO:0000269|PubMed:30270044, ECO:0000269|PubMed:32966796, ECO:0000269|PubMed:35532215, ECO:0000269|PubMed:35532216}.; FUNCTION: Can catalyze the transfer of adenosine 5'-monophosphate (AMP) to Ser, Thr and Tyr residues of target proteins (PubMed:30270044). In vitro, prefers ATP over other nucleotides as a cosubstrate (PubMed:30270044). Substrates include SelO itself, SucA, which is AMPylated on 'Thr-405', and GrxA, AMPylated on 'Tyr-13' (PubMed:30270044, PubMed:32966796). AMPylation of the grx family of enzymes may regulate protein S-glutathionylation levels in cells (PubMed:30270044). AMPylation is probably involved in redox homeostasis (PubMed:30270044)...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9). Activated by iscR (protein.P0AGK8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77649|protein.P77649]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=selO; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=selO; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005694,ECOCYC:G6924,GeneID:946219`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1789808-1791244:-; feature_type=gene
