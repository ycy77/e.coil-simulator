---
entity_id: "gene.b3623"
entity_type: "gene"
name: "waaU"
source_database: "NCBI RefSeq"
source_id: "gene-b3623"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3623"
  - "waaU"
---

# waaU

`gene.b3623`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3623`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

waaU (gene.b3623) is a gene entity. It encodes waaU (protein.P27242). Encoded protein function: FUNCTION: Transferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:1385388). May catalyze the addition of the terminal heptose (heptose IV) to the outer-core glucose III, the last step of the lipid A-core oligosaccharide biosynthesis (Probable). {ECO:0000269|PubMed:1385388, ECO:0000305|PubMed:9791168}. EcoCyc product frame: EG11423-MONOMER. EcoCyc synonyms: rfaK. Genomic coordinates: 3798239-3799312. EcoCyc protein note: WaaU is a putative ADP-heptose:LPS heptosyltransferase which may be responsible for the attachment of the fourth heptose residue (HepIV) residue to the third glucose (GlcIII) residue in the outer core of K-12 lipopolysaccharide; WaaU contains 2 glycosyltransferase motifs and shares regions of local similarity with the EG11189-MONOMER "WaaC" and EG12210 "WaaF" heptosyltransferases . O-antigen cannot be detected in the waaU (formerly rfaK) knockout mutant (rfaK2::ΩKMr) of an E. coli K-12 strain engineered to express Shigella dysenteriae O-antigen . WaaU is implicated in phage specificity: in contrast to the parental strain, an E. coli K-12 waaU knockout mutant is sensitive to the rough specific phage Br2; WaaU may be a transferase which adds N-acetyl D-glucosamine (GlcNAc) to an inner core heptose...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27242|protein.P27242]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=waaU; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011851,ECOCYC:EG11423,GeneID:948147`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3798239-3799312:-; feature_type=gene
