---
entity_id: "protein.P0AAB2"
entity_type: "protein"
name: "wzb"
source_database: "UniProt"
source_id: "P0AAB2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wzb b2061 JW2046"
---

# wzb

`protein.P0AAB2`

## Static

- Type: `protein`
- Source: `UniProt:P0AAB2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Dephosphorylates Wzc (PubMed:10348860). Required for the extracellular polysaccharide colanic acid synthesis, probably involved in the export of colanic acid from the cell to medium (PubMed:11090276). Involved in protection of cells against contact-dependent growth inhibition (CDI), probably due to the loss of a physical impediment to cell-cell contact. {ECO:0000269|PubMed:10348860, ECO:0000269|PubMed:11090276, ECO:0000269|PubMed:18761695}. Wzb is a protein-tyrosine phosphatase with activity towards autophosphorylated G7105-MONOMER "Wzc" protein . Autophosphorylation of Wzc negatively regulates colanic acid biosynthesis, and Wzb activity counteracts this negative regulation . Wzb acts on the phosphorylated tyrosine residues of the C-terminal tyrosine cluster in Wzc, but has little phosphatase activity toward the phosphorylated Y568 residue in Wzc . Wzb also does not exhibit significant phosphatase activity toward UDP-glucose dehydrogenase, a substrate of the Wzc kinase . The majority of the binding energy for the interaction between Wzb and the catalytic domain of Wzc appears to be provided by a region distinct from the phosphorylated C-tail of Wzc, instead overlapping with a region that plays a role in Wzc oligomerization and trans-phosphorylation...

## Biological Role

Catalyzes PROTEIN-TYROSINE-PHOSPHATASE-RXN (reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Dephosphorylates Wzc (PubMed:10348860). Required for the extracellular polysaccharide colanic acid synthesis, probably involved in the export of colanic acid from the cell to medium (PubMed:11090276). Involved in protection of cells against contact-dependent growth inhibition (CDI), probably due to the loss of a physical impediment to cell-cell contact. {ECO:0000269|PubMed:10348860, ECO:0000269|PubMed:11090276, ECO:0000269|PubMed:18761695}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN|reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2061|gene.b2061]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAB2`
- `KEGG:ecj:JW2046;eco:b2061;ecoc:C3026_11595;`
- `GeneID:93775130;946564;`
- `GO:GO:0000271; GO:0004725; GO:0009242`
- `EC:3.1.3.48`

## Notes

Low molecular weight protein-tyrosine-phosphatase Wzb (EC 3.1.3.48)
