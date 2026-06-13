---
entity_id: "gene.b2076"
entity_type: "gene"
name: "mdtC"
source_database: "NCBI RefSeq"
source_id: "gene-b2076"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2076"
  - "mdtC"
---

# mdtC

`gene.b2076`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2076`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtC (gene.b2076) is a gene entity. It encodes mdtC (protein.P76399). Encoded protein function: FUNCTION: The MdtABC tripartite complex confers resistance against novobiocin and deoxycholate. MdtABC requires TolC for its function. {ECO:0000255|HAMAP-Rule:MF_01424, ECO:0000269|PubMed:12107133, ECO:0000269|PubMed:12107134}. EcoCyc product frame: B2076-MONOMER. EcoCyc synonyms: yegO. Genomic coordinates: 2158386-2161463. EcoCyc protein note: MdtBC is the resistance-nodulation-division (RND) family permease of a tripartite efflux pump that is implicated in resistance to antibiotics, bile salt derivatives and SDS. MdtC contains 6 predicted transmembrane domains . MdtB and MdtC comprise a heteromultimeric transmembrane complex; the purified active complex contains MdtB and MdtC in a 2:1 ratio . The mdtC Keio collection mutant (BW25113 ΔmdtC::kan) shows a significant increase in swimming motility .

## Biological Role

Activated by cpxR (protein.P0AE88), baeR (protein.P69228).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76399|protein.P76399]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=mdtC; function=+
- `activates` <-- [[protein.P69228|protein.P69228]] `RegulonDB` `S` - regulator=BaeR; target=mdtC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006877,ECOCYC:G7115,GeneID:946608`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2158386-2161463:+; feature_type=gene
