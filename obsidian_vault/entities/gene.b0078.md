---
entity_id: "gene.b0078"
entity_type: "gene"
name: "ilvH"
source_database: "NCBI RefSeq"
source_id: "gene-b0078"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0078"
  - "ilvH"
---

# ilvH

`gene.b0078`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0078`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ilvH (gene.b0078) is a gene entity. It encodes ilvH (protein.P00894). Encoded protein function: Acetolactate synthase isozyme 3 small subunit (EC 2.2.1.6) (ALS-III) (Acetohydroxy-acid synthase III small subunit) (AHAS-III) EcoCyc product frame: ACETOLACTSYNIII-HCHAIN-MONOMER. EcoCyc synonyms: brnP. Genomic coordinates: 87357-87848. EcoCyc protein note: IlvH is the small regulatory subunit of the bifunctional acetohydroxybutanoate synthase /acetolactate synthase (IlvI/H, AHAS III) which carries out both the first step in valine biosynthesis and the second step in isoleucine biosynthesis. The IlvI/H protein complex catalyzes the conversion of pyruvate and oxobutanoate into 2-aceto-2-hydroxy-butyrate and the conversion of pyruvate into 2-acetolactate. Both reactions generate carbon dioxide as a product. IlvH confers sensitivity to inhibition by valine and is required for full catalytic activity of acetolactate synthase III holoenzyme . The crystal structure of IlvH has been determined at 1.75 Å resolution. It forms a dimer with two ferredoxin domains in each monomer. The valine binding sites can be tentatively assigned to the interface between the two N-terminal domains . C-terminal and N-terminal ilvH mutants were constructed and used to determine the minimum activation peptide necessary to activate IlvI...

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

- `encodes` --> [[protein.P00894|protein.P00894]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ilvH; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=ilvH; function=-+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=ilvH; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0000294,ECOCYC:EG10499,GeneID:947267`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:87357-87848:+; feature_type=gene
