---
entity_id: "gene.b2726"
entity_type: "gene"
name: "hypA"
source_database: "NCBI RefSeq"
source_id: "gene-b2726"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2726"
  - "hypA"
---

# hypA

`gene.b2726`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2726`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hypA (gene.b2726) is a gene entity. It encodes hypA (protein.P0A700). Encoded protein function: FUNCTION: Involved in the maturation of [NiFe] hydrogenases. Required for nickel insertion into the metal center of the hydrogenase (PubMed:12081959, PubMed:15995183). Mediates transfer of nickel, but not zinc, from the low-affinity metal-binding site in the GTPase domain of HypB to HypA (PubMed:23899293, PubMed:27951644). HypA is involved in maturation of hydrogenase 3. It may partially substitute for the function of HybF and vice versa (PubMed:12081959). May act as a scaffold for assembly of the nickel insertion proteins with the hydrogenase precursor protein after delivery of the iron center (PubMed:22016389). {ECO:0000269|PubMed:12081959, ECO:0000269|PubMed:15995183, ECO:0000269|PubMed:22016389, ECO:0000269|PubMed:23899293, ECO:0000269|PubMed:27951644}. EcoCyc product frame: EG10483-MONOMER. Genomic coordinates: 2850647-2850997. EcoCyc protein note: HypA and its homolog, HybF, are involved in the maturation of hydrogenase isozymes. A mutation in hypA almost completely abolishes hydrogenase 3 activity . HypA is specifically involved in hydrogenase 3 maturation, while HybF is involved in the maturation of hydrogenase 1 and 2; HypA and HybF can only partially substitute for each other...

## Biological Role

Activated by fhlA (protein.P19323), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A700|protein.P0A700]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=hypA; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=hypA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008958,ECOCYC:EG10483,GeneID:947195`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2850647-2850997:+; feature_type=gene
