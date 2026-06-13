---
entity_id: "gene.b3591"
entity_type: "gene"
name: "selA"
source_database: "NCBI RefSeq"
source_id: "gene-b3591"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3591"
  - "selA"
---

# selA

`gene.b3591`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3591`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

selA (gene.b3591) is a gene entity. It encodes selA (protein.P0A821). Encoded protein function: FUNCTION: Converts seryl-tRNA(Sec) to selenocysteinyl-tRNA(Sec) required for selenoprotein biosynthesis. Requires selenophosphate as the selenium-donor molecule. {ECO:0000269|PubMed:2007584, ECO:0000269|PubMed:2007585}. EcoCyc product frame: EG10941-MONOMER. EcoCyc synonyms: fdhA. Genomic coordinates: 3759858-3761249. EcoCyc protein note: Selenocysteine synthase (SelA) catalyzes the conversion of serine to selenocysteine on serine-charged tRNASec . SelA is a complex of 10 subunits with five-fold symmetry ; the homodecameric structure is assembled via stepwise addition of dimers to intermediate oligomeric states . Formation of a productive active site requires homodecamerization . The pyridoxal 5'-phosphate cofactor is present at a stoichiometry of one per monomer and is attached at Lys295 . The seryl-tRNASecUCA substrate was thought to be present at a stoichiometry of one per two monomers , but was later shown to be at a one-to-one stoichiometry . The serine residue of seryl-tRNASec first forms a Schiff base with the PLP cofactor, followed by dehydration of serine to generate the enzyme-bound aminoacrylyl-tRNASec intermediate . CPLX0-7957 SelD forms a ternary complex with the SelA-tRNASec complex...

## Biological Role

Repressed by selB (protein.P14081).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A821|protein.P0A821]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P14081|protein.P14081]] `RegulonDB` `C` - regulator=SelB-L-selenocysteinyl-tRNA<sup>sec</sup>; target=selA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011731,ECOCYC:EG10941,GeneID:948124`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3759858-3761249:-; feature_type=gene
