---
entity_id: "protein.P37760"
entity_type: "protein"
name: "rfbD"
source_database: "UniProt"
source_id: "P37760"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rfbD rmlD b2040 JW2025"
---

# rfbD

`protein.P37760`

## Static

- Type: `protein`
- Source: `UniProt:P37760`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the biosynthesis of the dTDP-L-rhamnose which is an important component of lipopolysaccharide (LPS) (Probable). Catalyzes the reduction of dTDP-6-deoxy-L-lyxo-4-hexulose to yield dTDP-L-rhamnose (By similarity). RmlD uses NADH and NADPH nearly equally well (By similarity). {ECO:0000250|UniProtKB:P26392, ECO:0000305|PubMed:7517391}. dTDP-4-dehydrorhamnose reductase (RfbD) is the final enzyme of the DTDPRHAMSYN-PWY pathway, which synthesizes one of the precursors for the O antigen of lipopolysaccharide. RfbD catalyzes the stereospecific reduction of the 4-keto group of dTDP-4-dehydro-6-deoxy-L-mannose to generate the final product, dTDP-L-rhamnose. The E. coli enzyme has not been biochemically characterized. E. coli K-12 strains carry mutations in the rfb gene cluster and do not produce O antigen. In MG1655, the rfb-50 allele, an IS5 insertion, interrupts the wbbL gene, which would encode the dTDP-rhamnose transferase . Deletion of rfbD enables increased production of quercetin 3-O-(6-deoxytalose) in an engineered E. coli strain . dTDP-4-dehydrorhamnose reductase has primarily been investigated in Salmonella enterica. The enzyme was purified and crystal structures have been obtained. A reaction mechanism was proposed, and predicted catalytic residues were tested by site-directed mutagenesis...

## Biological Role

Catalyzes DTDPDEHYRHAMREDUCT-RXN (reaction.ecocyc.DTDPDEHYRHAMREDUCT-RXN).

## Enriched Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of the dTDP-L-rhamnose which is an important component of lipopolysaccharide (LPS) (Probable). Catalyzes the reduction of dTDP-6-deoxy-L-lyxo-4-hexulose to yield dTDP-L-rhamnose (By similarity). RmlD uses NADH and NADPH nearly equally well (By similarity). {ECO:0000250|UniProtKB:P26392, ECO:0000305|PubMed:7517391}.

## Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DTDPDEHYRHAMREDUCT-RXN|reaction.ecocyc.DTDPDEHYRHAMREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2040|gene.b2040]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37760`
- `KEGG:ecj:JW2025;eco:b2040;ecoc:C3026_11490;`
- `GeneID:947117;`
- `GO:GO:0000271; GO:0005829; GO:0008831; GO:0009103; GO:0009243; GO:0019305; GO:0046872`
- `EC:1.1.1.133`

## Notes

dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133) (dTDP-4-keto-L-rhamnose reductase) (dTDP-6-deoxy-L-lyxo-4-hexulose reductase) (dTDP-6-deoxy-L-mannose dehydrogenase) (dTDP-L-rhamnose synthase)
