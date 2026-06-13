---
entity_id: "gene.b4476"
entity_type: "gene"
name: "gntU"
source_database: "NCBI RefSeq"
source_id: "gene-b4476"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4476"
  - "gntU"
---

# gntU

`gene.b4476`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4476`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gntU (gene.b4476) is a gene entity. It encodes gntU (protein.P0AC96). Encoded protein function: FUNCTION: Part of the gluconate utilization system Gnt-I; low-affinity intake of gluconate. EcoCyc product frame: GNTU-MONOMER. EcoCyc synonyms: b3435, b3436. Genomic coordinates: 3575721-3577061. EcoCyc protein note: GntU is one of four known transporters for gluconate in E. coli, the others being the homologous GntT, GntP and IdnT transporters. Whole cell experiments have shown that the cloned gntU gene was able to complement a gluconate transport negative mutant and confers low affinity gluconate transport with a Km of approx 212 μM . Transcriptional analysis has shown that gntU forms a dicistronic operon with the gntK gene encoding a gluconate kinase. Expression of gntU is induced by gluconate and controlled by the GntR repressor. GntU is a member of the Gnt family of gluconate transporters . Gluconate uptake has been reported to occur via a proton-symport mechanism in E. coli . It seems likely that GntU is a low affinity gluconate uptake system that functions via D-gluconate/proton symport.

## Biological Role

Repressed by gntR (protein.P0ACP5). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC96|protein.P0AC96]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gntU; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=gntU; function=+
- `represses` <-- [[protein.P0ACP5|protein.P0ACP5]] `RegulonDB` `C` - regulator=GntR; target=gntU; function=-

## External IDs

- `Dbxref:ASAP:ABE-0174105,ECOCYC:EG12631,GeneID:2847760`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3575721-3577061:-; feature_type=gene
