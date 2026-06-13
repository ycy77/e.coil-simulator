---
entity_id: "gene.b1616"
entity_type: "gene"
name: "uidB"
source_database: "NCBI RefSeq"
source_id: "gene-b1616"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1616"
  - "uidB"
---

# uidB

`gene.b1616`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1616`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uidB (gene.b1616) is a gene entity. It encodes uidB (protein.P0CE44). Encoded protein function: Glucuronide carrier protein homolog EcoCyc product frame: UIDB-MONOMER. EcoCyc synonyms: gusB, uidP. Genomic coordinates: 1692890-1694263. EcoCyc protein note: UidB, also known as GusB, is a proton-dependent transporter specific for α- and β-glucuronides . UidB is a member of the GPH family of galactose-pentose-hexuronide transporters . The uidB gene probably forms part of a three gene operon with uidA and uidC, encoding β-glucuronidase and a membrane protein, respectively. Imported β-glucuronides are cleaved by UidA to yield glucuronate. Expression studies and transport assays of GusBC in E. coli CE1 strain indicate that GusBC mediates the secondary active transport of glucuronide, which is energized by the respiration-generated proton motive force. Separate expression of the GusB protein shows that it is essential for glucuronide transport and is located in the inner membrane, while GusC is an outer membrane protein that can enhance glucuronide uptake by an unknown mechanism. GusC does not transport glucuronide . Functional evaluation of the GusBC transport system was carried out with genes from a natural E. coli isolate. The GusBC system in E. coli K-12 is nonfunctional. This appears to be due to the presence of a proline rather than a leucine at position 100 in GusB .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CE44|protein.P0CE44]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005407,ECOCYC:EG11658,GeneID:947484`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1692890-1694263:-; feature_type=gene
