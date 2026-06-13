---
entity_id: "gene.b0880"
entity_type: "gene"
name: "cspD"
source_database: "NCBI RefSeq"
source_id: "gene-b0880"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0880"
  - "cspD"
---

# cspD

`gene.b0880`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0880`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cspD (gene.b0880) is a gene entity. It encodes cspD (protein.P0A968). Encoded protein function: FUNCTION: Inhibits DNA replication at both initiation and elongation steps, most probably by binding to the opened, single-stranded regions at replication forks. Plays a regulatory role in chromosomal replication in nutrient-depleted cells.; FUNCTION: Involved in persister cell formation, acting downstream of mRNA interferase (toxin) MqsR. Overproduction is toxic. EcoCyc product frame: EG11111-MONOMER. EcoCyc synonyms: ybjA, cspH. Genomic coordinates: 922366-922590. EcoCyc protein note: CspD is a toxin that appears to act by inhibiting replication , and which influences persister cell formation . CspD forms a homodimer in solution, is able to bind single-stranded DNA and RNA, and packs ssDNA into structures that are distinguishable from SSB-coated DNA. Binding does not show sequence specificity. In vitro, CspD inhibits initiation and elongation of minichromosome replication . The CspD protein localizes to the nucleoid in stationary-phase cells . Expression of cspD is not inducible by cold shock and is inversely correlated with growth rate; it is induced at stationary phase and upon glucose starvation, but is not dependent on σS, the stationary phase sigma factor . Expression is upregulated by the golbal metabolic regulator CRP...

## Biological Role

Repressed by mqsA (protein.Q46864). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A968|protein.P0A968]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cspD; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=cspD; function=+
- `represses` <-- [[protein.Q46864|protein.Q46864]] `RegulonDB` `S` - regulator=MqsA; target=cspD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002991,ECOCYC:EG11111,GeneID:945669`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:922366-922590:-; feature_type=gene
