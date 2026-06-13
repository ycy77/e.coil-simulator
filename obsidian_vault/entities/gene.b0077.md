---
entity_id: "gene.b0077"
entity_type: "gene"
name: "ilvI"
source_database: "NCBI RefSeq"
source_id: "gene-b0077"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0077"
  - "ilvI"
---

# ilvI

`gene.b0077`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0077`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ilvI (gene.b0077) is a gene entity. It encodes ilvI (protein.P00893). Encoded protein function: Acetolactate synthase isozyme 3 large subunit (EC 2.2.1.6) (AHAS-III) (ALS-III) (Acetohydroxy-acid synthase III large subunit) EcoCyc product frame: ACETOLACTSYNIII-ICHAIN-MONOMER. Genomic coordinates: 85630-87354. EcoCyc protein note: IlvI is the large catalytic subunit of the bifunctional acetohydroxybutanoate synthase /acetolactate synthase (IlvI/H, AHAS III) which carries out both the first step in valine biosynthesis and the second step in isoleucine biosynthesis. The IlvI/H protein complex catalyzes the conversion of pyruvate and oxobutanoate into 2-aceto-2-hydroxy-butyrate and the conversion of pyruvate into 2-acetolactate. Both reactions generate carbon dioxide as a product. C-terminal and N-terminal ilvH mutants were constructed and used to determine the minimum activation peptide necessary to activate IlvI . Interactions between large and small subunits of different AHAS isozymes were investigated. IlvI could be activated by IlvM just as well as IlvH. Isolated IlvI has only 5% of the molar activity of its holoenzyme. However, isolated IlvI has similar substrate specificity and similar cofactor dependence as its holoenzyme. Assembly of the holoenzyme requires FAD.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00893|protein.P00893]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ilvI; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `C` - regulator=Lrp; target=ilvI; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=ilvI; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0000290,ECOCYC:EG10500,GeneID:948793`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:85630-87354:+; feature_type=gene
