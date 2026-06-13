---
entity_id: "gene.b3632"
entity_type: "gene"
name: "waaQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3632"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3632"
  - "waaQ"
---

# waaQ

`gene.b3632`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3632`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

waaQ (gene.b3632) is a gene entity. It encodes waaQ (protein.P25742). Encoded protein function: FUNCTION: Glycosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:25957775). Catalyzes the addition of the third heptose unit (HepIII) to the second heptose unit (HepII) of the phospho-Hep2-Kdo2-lipid A module (PubMed:25957775). {ECO:0000269|PubMed:25957775}. EcoCyc product frame: EG11341-MONOMER. EcoCyc synonyms: rfaQ. Genomic coordinates: 3807064-3808098. EcoCyc protein note: WaaQ is a heptosyltransferase that is responsible for addition of the side-branch heptose of the inner core of LPS . It catalyzes the transfer of L-glycero-D-manno-heptose to the second Hep of Hep2-Kdo2-Lipid A via an α(1→7) glycosidic linkage . A non-polar waaQ mutant lacks the HepIII sugar of the inner core region of LPS as well as phosphorylation at HepII . WaaP activity (phosphorylation at HepI) is a prerequisite for the efficient addition of the HepIII residue to the inner core by WaaQ . A waaQ transposon insertion mutant was shown to grow in mouse cecal mucus, but cell clumping appeared to prevent it from colonizing mouse large intestine. The mutant was also hypersensitive to sodium dodecyl sulfate, bile salts and novobiocin, as expected for deep-rough mutants...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25742|protein.P25742]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=waaQ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011870,ECOCYC:EG11341,GeneID:948155`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3807064-3808098:-; feature_type=gene
