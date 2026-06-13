---
entity_id: "gene.b0192"
entity_type: "gene"
name: "nlpE"
source_database: "NCBI RefSeq"
source_id: "gene-b0192"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0192"
  - "nlpE"
---

# nlpE

`gene.b0192`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0192`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nlpE (gene.b0192) is a gene entity. It encodes nlpE (protein.P40710). Encoded protein function: FUNCTION: Involved in copper homeostasis, could be involved in both copper efflux and the delivery of copper to copper-dependent enzymes (PubMed:7635807). Required for efficient binding of stationary phase cells to hydrophobic surfaces, part of the process of biofilm formation (PubMed:11830644). Functions during envelope stress responses; when overproduced induces degP through the activation of the two-component envelope stress response system CpxA/CpxR (PubMed:15252048, PubMed:7635808). DegP induction seems to require membrane anchoring of this protein (PubMed:15252048). Structural changes and/or interaction of the CXXC motif with its environment may lead to activation of the Cpx stress response (PubMed:17698001). {ECO:0000269|PubMed:11830644, ECO:0000269|PubMed:15252048, ECO:0000269|PubMed:17698001, ECO:0000269|PubMed:7635808}. EcoCyc product frame: EG12137-MONOMER. EcoCyc synonyms: cutF. Genomic coordinates: 215269-215979. EcoCyc protein note: NlpE is an outer membrane lipoprotein...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P40710|protein.P40710]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=nlpE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000652,ECOCYC:EG12137,GeneID:946782`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:215269-215979:+; feature_type=gene
