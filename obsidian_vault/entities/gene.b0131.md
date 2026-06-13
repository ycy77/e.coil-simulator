---
entity_id: "gene.b0131"
entity_type: "gene"
name: "panD"
source_database: "NCBI RefSeq"
source_id: "gene-b0131"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0131"
  - "panD"
---

# panD

`gene.b0131`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0131`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

panD (gene.b0131) is a gene entity. It encodes panD (protein.P0A790). Encoded protein function: FUNCTION: Catalyzes the pyruvoyl-dependent decarboxylation of aspartate to produce beta-alanine. {ECO:0000269|PubMed:6767707}. EcoCyc product frame: MONOMER0-1843. Genomic coordinates: 146314-146694. EcoCyc protein note: Aspartate 1-decarboxylase is responsible for the synthesis of β-alanine, which is needed in the biosynthesis of pantothenate. This enzyme is one of a small class of enzymes that use a covalently bound pyruvoyl prosthetic group. The pyruvoyl group is thought to act analogously to a pyridoxal phosphate cofactor by forming a Schiff base with the amino group of the substrate and then serving as an electron sink to facilitate the decarboxylation . Pyruvoyl-containing enzymes are expressed as a zymogen which is processed post-translationally by a self-maturation cleavage called serinolysis. E. coli contains two more such enzymes, PHOSPHASERDECARB-DIMER and SAMDECARB-CPLX. The PanD proenzyme (π protein) is processed at the serine residue at position 25, resulting in two subunits, α and β, which form a complex that is enzymatically active. Autocatalytic processing of purified enzyme preparations occurs slowly at room temperature or 37° C, and at a higher rate at elevated temperatures...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A790|protein.P0A790]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=panD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000459,ECOCYC:EG11747,GeneID:945686`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:146314-146694:-; feature_type=gene
