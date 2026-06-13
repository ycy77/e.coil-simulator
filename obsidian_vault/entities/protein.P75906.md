---
entity_id: "protein.P75906"
entity_type: "protein"
name: "pgaB"
source_database: "UniProt"
source_id: "P75906"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305|PubMed:18359807}; Lipid-anchor {ECO:0000305|PubMed:18359807}; Periplasmic side {ECO:0000305|PubMed:18359807}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pgaB ycdR b1023 JW5142"
---

# pgaB

`protein.P75906`

## Static

- Type: `protein`
- Source: `UniProt:P75906`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305|PubMed:18359807}; Lipid-anchor {ECO:0000305|PubMed:18359807}; Periplasmic side {ECO:0000305|PubMed:18359807}.

## Enriched Summary

FUNCTION: Catalyzes the N-deacetylation of poly-beta-1,6-N-acetyl-D-glucosamine (PGA), a biofilm adhesin polysaccharide. N-deacetylation promotes PGA export through the PgaA porin. {ECO:0000269|PubMed:15090514, ECO:0000269|PubMed:18359807}. PgaB is an outer membrane lipoprotein that is required for the partial de-N-acetylation and hydrolysis of poly-β-1,6-N-acetyl-D-glucosamine (known as PGA or PNAG) - an exopolysaccharide that is a key component of the biofilm matrix of many pathogenic bacteria . PgaB interacts with the outer membrane porin G6531-MONOMER PgaA and this interaction is implicated in the export of deacetylated PNAG . PgaB consists of an N-terminal deacetylase domain that has a distorted (β/α)7 barrel fold and belongs to the class 4 carbohydrate esterases and a C-terminal glycoside hydrolase (GH) domain that has a (β/α)8 barrel fold and belongs to a newly defined GH family - GH153 . Both domains are necessary for de-N-acetylation of PNAG; a cleft formed between the N and C-terminal domains is proposed to bind PNAG in an extended conformation during deacetylation . Full-length constructs of PgaB and the isolated GH domain both display glycoside hydrolase activity on partially deacetylated PNAG isolated from S. aureus . GH activity has been characterised in the Bordetella bronchiseptica isofunctional homolog (44% sequence identity)...

## Biological Role

Catalyzes RXN-19793 (reaction.ecocyc.RXN-19793), RXN0-5414 (reaction.ecocyc.RXN0-5414). Bound by Fe2+ (molecule.C14818).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Catalyzes the N-deacetylation of poly-beta-1,6-N-acetyl-D-glucosamine (PGA), a biofilm adhesin polysaccharide. N-deacetylation promotes PGA export through the PgaA porin. {ECO:0000269|PubMed:15090514, ECO:0000269|PubMed:18359807}.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-19793|reaction.ecocyc.RXN-19793]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5414|reaction.ecocyc.RXN0-5414]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1023|gene.b1023]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75906`
- `KEGG:ecj:JW5142;eco:b1023;ecoc:C3026_06220;`
- `GeneID:945604;`
- `GO:GO:0004553; GO:0005975; GO:0009279; GO:0016787; GO:0016810; GO:0043708; GO:0044010; GO:0098732`
- `EC:3.5.1.-`

## Notes

Poly-beta-1,6-N-acetyl-D-glucosamine N-deacetylase (PGA N-deacetylase) (Poly-beta-1,6-GlcNAc N-deacetylase) (EC 3.5.1.-)
