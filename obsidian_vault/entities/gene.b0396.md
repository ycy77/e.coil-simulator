---
entity_id: "gene.b0396"
entity_type: "gene"
name: "araJ"
source_database: "NCBI RefSeq"
source_id: "gene-b0396"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0396"
  - "araJ"
---

# araJ

`gene.b0396`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0396`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

araJ (gene.b0396) is a gene entity. It encodes araJ (protein.P23910). Encoded protein function: FUNCTION: May be involved in either the transport or processing of arabinose polymers. {ECO:0000305|PubMed:1744033}. EcoCyc product frame: ARAJ-MONOMER. EcoCyc synonyms: araT. Genomic coordinates: 411297-412481. EcoCyc protein note: AraJ is predicted to be an inner membrane protein with 12 transmembrane domains . Expression of araJ is induced in the presence of arabinose and transcription requires AraC and CRP-cAMP . Disruption of araJ does not have an apparent effect on arabinose uptake or utilisation . AraJ is not required for the intracellular arabinose depletion that is associated with 'off-switching' of the inducible arabinose utilization system . Heterologous expression of araJ enhances arabinose transport in a TAX-1142 strain engineered to utilize arabinose . In the Transporter Classification Database AraJ is a member of the Drug:H+ Antiporter-1 family within the Major Facilitator Superfamily .

## Biological Role

Repressed by crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), araC (protein.P0A9E0), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23910|protein.P23910]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=araJ; function=+
- `activates` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `S` - regulator=AraC; target=araJ; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=araJ; function=-+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=araJ; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0001378,ECOCYC:EG10060,GeneID:949077`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:411297-412481:-; feature_type=gene
