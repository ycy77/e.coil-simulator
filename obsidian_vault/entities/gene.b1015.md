---
entity_id: "gene.b1015"
entity_type: "gene"
name: "putP"
source_database: "NCBI RefSeq"
source_id: "gene-b1015"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1015"
  - "putP"
---

# putP

`gene.b1015`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1015`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

putP (gene.b1015) is a gene entity. It encodes putP (protein.P07117). Encoded protein function: FUNCTION: Catalyzes the sodium-dependent uptake of extracellular L-proline (PubMed:1567896, PubMed:3512540, PubMed:9693004). This protein is also capable of using lithium as the transport cation (PubMed:1567896, PubMed:9693004). Also catalyzes the uptake of propionate (PubMed:17088549). {ECO:0000269|PubMed:1567896, ECO:0000269|PubMed:17088549, ECO:0000269|PubMed:3512540, ECO:0000269|PubMed:9693004}. EcoCyc product frame: PUTP-MONOMER. EcoCyc synonyms: putC. Genomic coordinates: 1079305-1080813. EcoCyc protein note: PutP is a member of the SSS family of sodium/solute transporters . PutP is a sodium/proline symporter responsible for the uptake of proline. Mutations in putP decrease proline transport and can be complemented by the cloned putP gene . The PutP protein has been purified, reconstituted into proteoliposomes, and shown to mediate proline transport in the presence of a sodium or lithium ion gradient . Mutant phenotype and expression analysis also suggest that PutP may be responsible for the transport of the short chain fatty acid propionate . Kinetic analysis has shown that PutP binds proline with a Km of approximately 2 μM and sodium with a Km of approximately 700 μM . Sodium and proline are transported by PutP with a stoichiometry of 1:1...

## Biological Role

Repressed by putA (protein.P09546), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07117|protein.P07117]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=putP; function=+
- `represses` <-- [[protein.P09546|protein.P09546]] `RegulonDB` `C` - regulator=PutA; target=putP; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=putP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003433,ECOCYC:EG10802,GeneID:945602`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1079305-1080813:+; feature_type=gene
