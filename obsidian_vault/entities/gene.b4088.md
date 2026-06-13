---
entity_id: "gene.b4088"
entity_type: "gene"
name: "alsB"
source_database: "NCBI RefSeq"
source_id: "gene-b4088"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4088"
  - "alsB"
---

# alsB

`gene.b4088`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4088`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alsB (gene.b4088) is a gene entity. It encodes alsB (protein.P39265). Encoded protein function: FUNCTION: Part of the binding-protein-dependent transport system AlsBAC for D-allose. {ECO:0000269|PubMed:9401019}. EcoCyc product frame: YJCX-MONOMER. EcoCyc synonyms: yjcX. Genomic coordinates: 4311107-4312042. EcoCyc protein note: AlsB is the periplasmic binding protein of a D-allose ATP-binding cassette (ABC) transport system. AlsB binds D-allose with high affinity (KD = 0.33 µM) . A crystal structure of AlsB bound to D-allose has been reported ; the protein contains two α/β domains joined by a 3 stranded hinge and adopts a closed conformation in which a β D-allopyranose form of the sugar is buried at the interface between the two domains. Ligand free structures of AlsB adopt a conformation in which the interface between the two domains is opened up to the solvent; conformational change between ligand free (open) and liganded (closed) forms is associated with movement of the hinge . Overexpression of alsB increases the tolerance of E. coli to n-butanol .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39265|protein.P39265]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=alsB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013398,ECOCYC:EG12458,GeneID:948604`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4311107-4312042:-; feature_type=gene
