---
entity_id: "protein.P08191"
entity_type: "protein"
name: "fimH"
source_database: "UniProt"
source_id: "P08191"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Fimbrium {ECO:0000269|PubMed:1971261}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fimH b4320 JW4283"
---

# fimH

`protein.P08191`

## Static

- Type: `protein`
- Source: `UniProt:P08191`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Fimbrium {ECO:0000269|PubMed:1971261}.

## Enriched Summary

FUNCTION: Involved in regulation of length and mediation of adhesion of type 1 fimbriae (but not necessary for the production of fimbriae). Adhesin responsible for the binding to D-mannose. It is laterally positioned at intervals in the structure of the type 1 fimbriae. In order to integrate FimH in the fimbriae FimF and FimG are needed. {ECO:0000269|PubMed:1971261}. Type 1, or mannose-sensitive, fimbriae in Escherichia coli mediate binding to receptor structures allowing the bacteria to colonize various host tissues. Receptor recognition is a function of the FimH adhesin of the fimbriae . FimH protein is located both at the tip of the fimbria as well as interspersed along the shaft . Two-dimensional gel electrophoresis suggests that FimH has a molecular weight of 30 kDa and is present in a 1:100 ratio with the major fimbrial subunit, FimA . The binding phenotype of type 1 fimbriae is sensitive to minor amino acid changes in the FimH protein . Mutational studies have identified residues important for the interaction between FimD, an usher involved in fimbriae polymerization, and FimH . The x-ray structure of the FimC-FimH chaperone-adhesin complex from uropathogenic E. coli has been determined to 2.5 Å resolution . A crystal structure of FimH integrated into the fimbrial tips (a FimCFGH complex) has been resolved at 2...

## Biological Role

Component of fimbrial complex (complex.ecocyc.CPLX0-3401).

## Annotation

FUNCTION: Involved in regulation of length and mediation of adhesion of type 1 fimbriae (but not necessary for the production of fimbriae). Adhesin responsible for the binding to D-mannose. It is laterally positioned at intervals in the structure of the type 1 fimbriae. In order to integrate FimH in the fimbriae FimF and FimG are needed. {ECO:0000269|PubMed:1971261}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3401|complex.ecocyc.CPLX0-3401]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4320|gene.b4320]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08191`
- `KEGG:ecj:JW4283;eco:b4320;ecoc:C3026_23335;`
- `GeneID:948847;`
- `GO:GO:0005537; GO:0007155; GO:0007638; GO:0009289; GO:0009419; GO:0031589; GO:0033644; GO:0043709`

## Notes

Type 1 fimbrin D-mannose specific adhesin (Protein FimH)
