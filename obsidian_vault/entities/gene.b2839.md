---
entity_id: "gene.b2839"
entity_type: "gene"
name: "lysR"
source_database: "NCBI RefSeq"
source_id: "gene-b2839"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2839"
  - "lysR"
---

# lysR

`gene.b2839`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2839`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lysR (gene.b2839) is a gene entity. It encodes lysR (protein.P03030). Encoded protein function: FUNCTION: This protein activates the transcription of the lysA gene encoding diaminopimelate decarboxylase. LysR is also a negative regulator of its own expression. EcoCyc product frame: PD00360. Genomic coordinates: 2979021-2979956. EcoCyc protein note: "Lysine Regulator," LysR, is negatively autoregulated and coordinately activates transcription of the divergent gene which encodes the enzyme that catalyzes the last step in lysine biosynthesis . Activation by LysR requires the presence of diaminopimelic acid . Stragier et al. have proposed that this compound binds directly with LysR . LysR belongs to the family LysR, which contains three domains : an amino-terminal domain that contains a potential helix-turn-helix DNA-binding motif; a central domain, with response domains much less conserved, that possibly are important for coinducer-responsive transcription; and a C-terminal domain that includes the key residues possibly involved in DNA interactions and coinducer response . In systematic studies of oligomerization, it was shown that some members of the LysR family, like LysR, interact with other members of the family to form heterodimers, but the physiological significance of this is unknown...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03030|protein.P03030]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=lysR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009313,ECOCYC:EG10551,GeneID:947311`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2979021-2979956:+; feature_type=gene
