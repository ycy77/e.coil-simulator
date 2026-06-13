---
entity_id: "gene.b2988"
entity_type: "gene"
name: "gss"
source_database: "NCBI RefSeq"
source_id: "gene-b2988"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2988"
  - "gss"
---

# gss

`gene.b2988`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2988`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gss (gene.b2988) is a gene entity. It encodes gss (protein.P0AES0). Encoded protein function: FUNCTION: Catalyzes the formation of an amide bond between glutathione (GSH) and spermidine coupled with hydrolysis of ATP; also catalyzes the opposing reaction, i.e. the hydrolysis of glutathionylspermidine (Gsp) back to glutathione and spermidine. The amidase active site can also hydrolyze Gsp-disulfide (Gsp-S-S-Gsp) to Gsp-SG and Gsp S-thiolated proteins (GspSSPs) to GSH S-thiolated protein (GSSPs). Likely acts synergistically with glutaredoxin to regulate the redox environment of E.coli and defend against oxidative damage. In vitro, the amidase active site also catalyzes hydrolysis of amide and ester derivatives of glutathione (e.g. glutathione ethyl ester and glutathione amide) but lacks activity toward acetylspermidine (N1 and N8) and acetylspermine (N1). {ECO:0000269|PubMed:20530482, ECO:0000269|PubMed:23097746, ECO:0000269|PubMed:7775463, ECO:0000269|PubMed:8999955}. EcoCyc product frame: GSP-MONOMER. EcoCyc synonyms: gsp. Genomic coordinates: 3136663-3138522. EcoCyc protein note: gss encodes a bifunctional protein with two domains: an N-terminal glutathionylspermidine (GSP) amidase domain and a C-terminal GSP synthetase domain. The enzyme catalyzes both the formation and hydrolysis of an amide bond between glutathione and spermidine...

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AES0|protein.P0AES0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009804,ECOCYC:EG12882,GeneID:947474`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3136663-3138522:-; feature_type=gene
