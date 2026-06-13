---
entity_id: "gene.b1260"
entity_type: "gene"
name: "trpA"
source_database: "NCBI RefSeq"
source_id: "gene-b1260"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1260"
  - "trpA"
---

# trpA

`gene.b1260`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1260`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trpA (gene.b1260) is a gene entity. It encodes trpA (protein.P0A877). Encoded protein function: FUNCTION: The alpha subunit is responsible for the aldol cleavage of indoleglycerol phosphate to indole and glyceraldehyde 3-phosphate. EcoCyc product frame: TRYPSYN-APROTEIN. EcoCyc synonyms: try, tryp. Genomic coordinates: 1316416-1317222. EcoCyc protein note: The TrpA polypeptide (TSase α) functions as the α subunit of the tetrameric (α2-β2) tryptophan synthase complex . As a purified protein, the α subunit is a monomer. TSase α contains the binding site for indole-3-glycerol-phosphate (InGP) and can carry out the cleavage reaction of InGP to indole and glyceraldehyde-3-phosphate, also termed the α reaction. Within the physiological complex with the β subunit, the reaction rate is increased by 1-2 orders of magnitude (in ). TrpA has been shown to lack tryptophan residues . Numerous TrpA mutant studies have examined structure-function relationships in this protein. Mutations that affect catalytic activity , subunit interactions , conformational stability and folding have been identified. The crystal structure of the wild-type TrpA protein has been reported at 2.8 Å resolution , 2.5 Å resolution and 2.3 Å resolution . The crystal structure of a double mutant TrpA protein has been reported at 1.8 Å resolution...

## Biological Role

Repressed by trpR (protein.P0A881). Activated by rydC (gene.b4597), rpoD (protein.P00579).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A877|protein.P0A877]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[gene.b4597|gene.b4597]] `RegulonDB` `S` - regulator=RydC; target=trpA; function=+
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=trpA; function=+
- `represses` <-- [[protein.P0A881|protein.P0A881]] `RegulonDB` `C` - regulator=TrpR; target=trpA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004232,ECOCYC:EG11024,GeneID:946204`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1316416-1317222:-; feature_type=gene
