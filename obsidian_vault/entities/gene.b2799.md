---
entity_id: "gene.b2799"
entity_type: "gene"
name: "fucO"
source_database: "NCBI RefSeq"
source_id: "gene-b2799"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2799"
  - "fucO"
---

# fucO

`gene.b2799`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2799`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fucO (gene.b2799) is a gene entity. It encodes fucO (protein.P0A9S1). Encoded protein function: Lactaldehyde reductase (EC 1.1.1.77) (Propanediol oxidoreductase) EcoCyc product frame: LACTALDREDUCT-MONOMER. Genomic coordinates: 2931865-2933013. EcoCyc protein note: L-1,2-propanediol oxidoreductase is an iron-dependent group III dehydrogenase. It anaerobically reduces L-lactaldehyde, a product of both the L-fucose and L-rhamnose catabolic pathways, to L-1,2-propanediol, which is then excreted from the cell . A mutant's ability to grow on L-1,2-propanediol as the source of carbon and energy is due to constitutive production of FucO, and the enzyme then serves as a propanediol dehydrogenase . Another mutant strain was selected for the ability to utilize ethylene glycol as a carbon source. This ability is in part due to a regulatory mutation that increases the activity of FucO, which can utilize ethylene glycol as an alternate substrate . Crystal structures of the enzyme have been solved, showing a domain-swapped dimer in which the metal, cofactor and substrate binding sites could be located . An aspartate and three conserved histidine residues are required for Fe2+ binding and enzymatic activity . The stereoselectivity of the enzyme has been explained by a critical hydrogen bond interaction between the (2S)-hydroxyl and the side-chain of N151...

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), fucR (protein.P0ACK8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9S1|protein.P0A9S1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fucO; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=fucO; function=+
- `activates` <-- [[protein.P0ACK8|protein.P0ACK8]] `RegulonDB` `S` - regulator=FucR; target=fucO; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=fucO; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009177,ECOCYC:EG10351,GeneID:947273`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2931865-2933013:-; feature_type=gene
