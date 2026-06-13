---
entity_id: "protein.P32662"
entity_type: "protein"
name: "gph"
source_database: "UniProt"
source_id: "P32662"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gph yhfE b3385 JW3348"
---

# gph

`protein.P32662`

## Static

- Type: `protein`
- Source: `UniProt:P32662`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Specifically catalyzes the dephosphorylation of 2-phosphoglycolate (2P-Gly). Is involved in the dissimilation of the intracellular 2-phosphoglycolate formed during the DNA repair of 3'-phosphoglycolate ends, a major class of DNA lesions induced by oxidative stress. {ECO:0000269|PubMed:16990279}. The gph gene encodes a haloacid dehalogenase (HAD)-like phosphatase family enzyme with 2-phosphoglycolate phosphatase activity . 2-phosphoglycolate phosphatase is an enzyme of the Calvin Cycle for assimilation of CO2, and it was thus not clear why it would be found in E. coli . However, 2-phosphoglycolate is formed during repair of DNA strand breaks with 3'-phosphoglycolate ends; such breaks can be caused by radiomimetic drugs like bleomycin . Gph was shown to be involved in the recovery of glycolate from 2-phosphoglycolate released by the activity of DNA repair enzymes after bleomycin treatment . Deletion of gph resulted in loss of induction of the glc operon by glycolate after bleomycin treatment . gph mutants also failed to recover as quickly as wild type after bleomycin treatment . In a previous study gph deletion mutation had no apparent physiological effect . Expression of gph appears to be constitutive . Overexpression of the EG11871 gene is able to rescue a mutation in the EG10945 gene . Gph: "phosphoglycolate phosphatase"

## Biological Role

Catalyzes GPH-RXN (reaction.ecocyc.GPH-RXN). Bound by Magnesium cation (molecule.C00305), chloride (molecule.ecocyc.CL-).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Specifically catalyzes the dephosphorylation of 2-phosphoglycolate (2P-Gly). Is involved in the dissimilation of the intracellular 2-phosphoglycolate formed during the DNA repair of 3'-phosphoglycolate ends, a major class of DNA lesions induced by oxidative stress. {ECO:0000269|PubMed:16990279}.

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GPH-RXN|reaction.ecocyc.GPH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CL-|molecule.ecocyc.CL-]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3385|gene.b3385]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32662`
- `KEGG:ecj:JW3348;eco:b3385;ecoc:C3026_18370;`
- `GeneID:947895;`
- `GO:GO:0000287; GO:0005829; GO:0005975; GO:0006281; GO:0008967; GO:0031404; GO:0046295`
- `EC:3.1.3.18`

## Notes

Phosphoglycolate phosphatase (PGP) (PGPase) (EC 3.1.3.18)
