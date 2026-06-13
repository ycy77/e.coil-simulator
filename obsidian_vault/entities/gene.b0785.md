---
entity_id: "gene.b0785"
entity_type: "gene"
name: "moaE"
source_database: "NCBI RefSeq"
source_id: "gene-b0785"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0785"
  - "moaE"
---

# moaE

`gene.b0785`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0785`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

moaE (gene.b0785) is a gene entity. It encodes moaE (protein.P30749). Encoded protein function: FUNCTION: Converts molybdopterin precursor Z to molybdopterin. This requires the incorporation of two sulfur atoms into precursor Z to generate a dithiolene group. The sulfur is provided by MoaD. EcoCyc product frame: EG11598-MONOMER. EcoCyc synonyms: chlA5. Genomic coordinates: 819295-819747. EcoCyc protein note: Site-directed mutagenesis and in vitro assays of wild-type and mutant MoaE proteins showed that amino acid residues Lys-119, Arg-39 and Lys-126 are critical for molybdopterin synthase activity . Within the MoaDE complex the two MoaE subunits form a central dimer and each of the two MoaD subunits are located at the opposite ends of the dimer . The crystal structure of a homodimeric MoaE deletion mutant in the absence of MoaD was determined at 2.15 Å resolution . In E. coli K-12, moaE, mog (mogA), moaA, moaB, modB, or modC deletion mutants lose the ability to reduce CPD-4544 (tellurate), which could be restored by complementation. Although the E. coli tellurate reductase gene and its product remain uncharacterized, these data suggest that it involves a molybdoenzyme...

## Biological Role

Activated by fnr (protein.P0A9E5), modE (protein.P0A9G8), csrA (protein.P69913).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30749|protein.P30749]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=moaE; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=moaE; function=+
- `activates` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `C` - regulator=CsrA; target=moaE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002678,ECOCYC:EG11598,GeneID:945399`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:819295-819747:+; feature_type=gene
