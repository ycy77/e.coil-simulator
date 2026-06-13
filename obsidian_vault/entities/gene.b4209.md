---
entity_id: "gene.b4209"
entity_type: "gene"
name: "ytfE"
source_database: "NCBI RefSeq"
source_id: "gene-b4209"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4209"
  - "ytfE"
---

# ytfE

`gene.b4209`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4209`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ytfE (gene.b4209) is a gene entity. It encodes ytfE (protein.P69506). Encoded protein function: FUNCTION: Di-iron-containing protein involved in the repair of iron-sulfur clusters damaged by oxidative and nitrosative stress conditions. {ECO:0000269|PubMed:16553864, ECO:0000269|PubMed:17289666, ECO:0000269|PubMed:18357473}. EcoCyc product frame: G7866-MONOMER. EcoCyc synonyms: dnrN. Genomic coordinates: 4431321-4431983. EcoCyc protein note: YtfE belongs to a conserved and widely distributed family of hemerythrin-like proteins. Purified YtfE contains a non-heme di-iron center of the histidine-carboxylate type . Based on spectroscopic, mass spectrometric and kinetic approaches, YtfE is considered to belong to a new class of nitrite reductases . YtfE appears to be involved in the repair of iron centers . YtfE is able to donate iron for the assembly of an Fe-S cluster into apo-G7324-MONOMER IscU but only under conditions that degrade its di-iron center . YtfE can also act as a nitric oxide scavenger that catalyzes the reduction of nitric oxide (NO) to nitrous oxide (N2O) . Genetic interaction experiments suggest that YtfE releases NO from nitrosylation-damaged metalloproteins, with subsequent reduction of NO to N2O by the G6457-MONOMER hybrid cluster protein . Similarly, in the absence of EG11415-MONOMER Dps, YtfE increases the intracellular levels of reactive oxygen species...

## Biological Role

Repressed by nsrR (protein.P0AF63).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69506|protein.P69506]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0AF63|protein.P0AF63]] `RegulonDB` `S` - regulator=NsrR; target=ytfE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013766,ECOCYC:G7866,GeneID:948724`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4431321-4431983:-; feature_type=gene
