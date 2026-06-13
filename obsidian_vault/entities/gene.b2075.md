---
entity_id: "gene.b2075"
entity_type: "gene"
name: "mdtB"
source_database: "NCBI RefSeq"
source_id: "gene-b2075"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2075"
  - "mdtB"
---

# mdtB

`gene.b2075`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2075`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtB (gene.b2075) is a gene entity. It encodes mdtB (protein.P76398). Encoded protein function: FUNCTION: The MdtABC tripartite complex confers resistance against novobiocin and deoxycholate. MdtABC requires TolC for its function. {ECO:0000255|HAMAP-Rule:MF_01423, ECO:0000269|PubMed:12107133, ECO:0000269|PubMed:12107134}. EcoCyc product frame: B2075-MONOMER. EcoCyc synonyms: yegN. Genomic coordinates: 2155263-2158385. EcoCyc protein note: MdtBC is the resistance-nodulation-division (RND) family permease of a tripartite efflux pump that is implicated in resistance to antibiotics, bile salt derivatives and SDS. MdtB contains 6 predicted transmembrane domains . MdtB and MdtC comprise a heteromultimeric transmembrane complex; the purified active complex contains MdtB and MdtC in a 2:1 ratio . mdtB is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function . The mdtB Keio collection mutant (BW25113 ΔmdtB::kan) shows a significant increase in swimming motility .

## Biological Role

Activated by cpxR (protein.P0AE88), baeR (protein.P69228).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76398|protein.P76398]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=mdtB; function=+
- `activates` <-- [[protein.P69228|protein.P69228]] `RegulonDB` `S` - regulator=BaeR; target=mdtB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006874,ECOCYC:G7114,GeneID:946606`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2155263-2158385:+; feature_type=gene
