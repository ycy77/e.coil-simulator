---
entity_id: "gene.b3960"
entity_type: "gene"
name: "argH"
source_database: "NCBI RefSeq"
source_id: "gene-b3960"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3960"
  - "argH"
---

# argH

`gene.b3960`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3960`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argH (gene.b3960) is a gene entity. It encodes argH (protein.P11447). Encoded protein function: Argininosuccinate lyase (ASAL) (EC 4.3.2.1) (Arginosuccinase) EcoCyc product frame: ARGSUCCINLYA-MONOMER. Genomic coordinates: 4156850-4158223. EcoCyc protein note: Argininosuccinate lyase catalyzes the final step in the L-arginine biosynthesis pathway. A crystal structure of argininosuccinate lyase has been solved at 2.44 Å resolution; the enzyme appears to be tetrameric, with a dimer as the asymmetric unit of this crystal form . ArgH expression is repressed by the addition of arginine or ornithine to the medium .

## Biological Role

Repressed by argR (protein.P0A6D0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11447|protein.P11447]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=argH; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=argH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012969,ECOCYC:EG11223,GeneID:948463`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4156850-4158223:+; feature_type=gene
