---
entity_id: "protein.P0ACD4"
entity_type: "protein"
name: "iscU"
source_database: "UniProt"
source_id: "P0ACD4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "iscU nifU yfhN b2529 JW2513"
---

# iscU

`protein.P0ACD4`

## Static

- Type: `protein`
- Source: `UniProt:P0ACD4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A scaffold on which IscS assembles Fe-S clusters. Exists as 2 interconverting forms, a structured (S) and disordered (D) form. The D-state is the preferred substrate for IscS. Converts to the S-state when an Fe-S cluster is assembled, which helps it dissociate from IscS to transfer the Fe-S to an acceptor. It is likely that Fe-S cluster coordination is flexible as the role of this complex is to build and then hand off Fe-S clusters. {ECO:0000269|PubMed:11577100, ECO:0000269|PubMed:22203963}. The assembly of iron-sulfur clusters requires complex biosynthetic machinery. E. coli encodes two sets of proteins, the Isc and the Suf system, to achieve this task. IscU is the scaffold protein for assembly and transfer of iron-sulfur clusters of the Isc system. The cysteine desulfurase CPLX0-248 IscS transfers the sulfane sulfur to IscU, EG12132-MONOMER IscA acts as the iron chaperone, EG11653-MONOMER CyaY appears to regulate cluster assembly, and the EG12130-MONOMER HscA and EG12131-MONOMER HscB chaperone and cochaperone facilitate Fe-S cluster transfer. An iron-first mechanism for Fe-S cluster assembly has been proposed . The C terminus of IscS interacts with IscU and transfers sulfur directly to IscU . The mechanism of transfer is discussed...

## Biological Role

Catalyzes RXN-25083 (reaction.ecocyc.RXN-25083).

## Annotation

FUNCTION: A scaffold on which IscS assembles Fe-S clusters. Exists as 2 interconverting forms, a structured (S) and disordered (D) form. The D-state is the preferred substrate for IscS. Converts to the S-state when an Fe-S cluster is assembled, which helps it dissociate from IscS to transfer the Fe-S to an acceptor. It is likely that Fe-S cluster coordination is flexible as the role of this complex is to build and then hand off Fe-S clusters. {ECO:0000269|PubMed:11577100, ECO:0000269|PubMed:22203963}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-25083|reaction.ecocyc.RXN-25083]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2529|gene.b2529]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACD4`
- `KEGG:ecj:JW2513;eco:b2529;ecoc:C3026_14015;`
- `GeneID:86860655;93774607;947002;`
- `GO:GO:0005507; GO:0005737; GO:0005829; GO:0006879; GO:0008198; GO:0008270; GO:0016226; GO:0019448; GO:0042802; GO:0051537; GO:0051539; GO:1990330`

## Notes

Iron-sulfur cluster assembly scaffold protein IscU (Sulfur acceptor protein IscU)
